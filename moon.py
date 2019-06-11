import time
import re
import weather_util as util

class Moon:
    def forecast_get(self, html):
        split_htmls = html.split('\n')

        for split_html in split_htmls:
            if split_html.find('<section class="forecast"') != -1:
                return split_html

    def __init__(self, uri):
        self.moons = []

        html = util.html_get(uri)

        forecast = self.forecast_get(html)

        moons = forecast.split('datetime=')
        for moon in moons:
            moon_match = re.findall(r'([0-9\-]+)".+data-fill="([0-9]+)"', moon)
            if len(moon_match) < 1:
                continue
            moon_list = list(moon_match[0])
            moon_list[0] = util.time_get(moon_list[0])
            self.moons.append(list(moon_list))

    def get(self, start=0, end=3600*24*365*100000):
        result = []
        for moon in self.moons:
            if moon[0] >= start and moon[0] < end:
                result.append(moon)
        return result

    def print(self, start=0, end=3600*24*365*100000):
        results = self.get(start, end)
        print ("moon: ", end="")
        for result in results:
            print("{}%".format(result[1]))
            

if __name__ == "__main__":
    moon = Moon(r"https://moonphases.willyweather.com.au/nsw/sydney/sydney.html")
    moon.print()
