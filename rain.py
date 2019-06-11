import time
import re
import weather_util as util

class Rain:
    def forecast_get(self, html):
        split_htmls = html.split('\n')

        for split_html in split_htmls:
            if split_html.find('<section class="forecast selectable">') != -1:
                return split_html

    def __init__(self, uri):
        self.rains = []

        html = util.html_get(uri)

        forecast = self.forecast_get(html)

        rains = forecast.split('datetime=')

        for rain in rains[1:]:
            rain_match = re.findall(r'"([0-9\-]+)".+chance-value">([0-9]+%).+"chance-amount amount-[0-9\-]+">(.+)</b>', rain)
            if len(rain_match) > 0:
                rain_match = list(rain_match[0])
                rain_match[2] = rain_match[2].replace('&lt;', '<')
                rain_match[2] = rain_match[2].replace('&gt;', '>')
                rain_match[2] = rain_match[2].replace('&nbsp;', ' ')
                rain_match[2] = rain_match[2].replace('&ndash;', '-')
            else:
                rain_match = re.findall(r'"([0-9\-]+)".+No Rain', rain)
                if len(rain_match) == 0:
                    continue
                rain_match.append('0%')
                rain_match.append('0mm')
            rain_match[0] = util.time_get(rain_match[0])
            self.rains.append(rain_match)

    def get(self, start=0, end=3600*24*365*100000):
        result = []
        for rain in self.rains:
            if rain[0] >= start and rain[0] < end:
                result.append(rain)
        return result

    def print(self, start=0, end=3600*24*365*100000):
        results = self.get(start, end)
        print ("rain: ", end="")
        for result in results:
            print("{}, {}".format(result[1], result[2]))


if __name__ == "__main__":
    rain = Rain(r"https://rainfall.willyweather.com.au/nsw/sydney/sydney.html")
    rain.print()
    