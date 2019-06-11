import time
import re
import weather_util as util

class Swell:
    def forecast_heights_get(self, html):
        parts = re.findall(r'"id":"swell-height".+"id":"swell-period"', html)
        return parts[0]

    def forecast_periods_get(self, html):
        parts = re.findall(r'"id":"swell-period".+', html)
        return parts[0]

    def heights_get(self, forecast_height):
        datas = re.findall(r'{"x":([0-9]+),"y":([0-9.]+),"direction":[0-9.]+,"directionText":"([NEWS]+)"', forecast_height)
        heights = []
        for data in datas:
            data_list = list(data)
            data_list[0] = int(data_list[0])
            heights.append(data_list)
        return heights

    def periods_get(self, forecast_period):
        datas = re.findall(r'{"x":([0-9]+),"y":([0-9.]+)', forecast_period)
        periods = []
        for data in datas:
            data_list = list(data)
            data_list[0] = int(data_list[0])
            periods.append(list(data_list))
        return periods

    def merge(self, heights, periods):
        swells = []
        for height in heights:
            for period in periods:
                if height[0] == period[0]:
                    height.append(period[1])
                    swells.append(height)
        return swells

    def __init__(self, uri):

        html = util.html_get(uri)

        forecast_heights = self.forecast_heights_get(html)
        heights = self.heights_get(forecast_heights)
        
        forecast_periods = self.forecast_periods_get(html)
        periods = self.periods_get(forecast_periods)

        self.swells = self.merge(heights, periods)
        
        
    def get(self, start=0, end=3600*24*365*100000):
        result = []
        for swell in self.swells:
            if swell[0] >= start and swell[0] < end:
                result.append(swell)
        return result

    def print(self, start=0, end=3600*24*365*100000):
        results = self.get(start, end)
        print ("swell: ", end="")
        for result in results:
            print(result)
        print("")

if __name__ == "__main__":
    swell = Swell(r"https://swell.willyweather.com.au/nsw/sydney/south-head.html")
    swell.print()
    