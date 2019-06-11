import time
import re
import weather_util as util

class Wind:
    def forecast_get(self, html):
        parts = re.findall(r'data: {"forecastGraphs".+}}}}}}}', html)
        return parts[0]

    def __init__(self, uri):
        self.winds = []
        html = util.html_get(uri)
        forecast = self.forecast_get(html)
        datas = re.findall(r'{"x":([0-9]+),"y":([0-9.]+),"direction":[0-9]+,"directionText":"([NEWS]+)",', forecast)
        for data in datas:
            data_list = list(data)
            data_list[0] = int(data_list[0])
            self.winds.append(data_list)

    def get(self, start=0, end=3600*24*365*100000):
        result = []
        for wind in self.winds:
            if wind[0] >= start and wind[0] < end:
                result.append(wind)
        return result

    def print(self, start=0, end=3600*24*365*100000):
        results = self.get(start, end)
        print ("wind: ", end="")
        for result in results:
            print(result)
        print("")

if __name__ == "__main__":
    wind = Wind(r"sample\wind.html")
    wind.print()
