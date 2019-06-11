import time
import re
import weather_util as util

class Tide:
    def forecast_get(self, html):
        return html

    def __init__(self, uri):
        self.tides = []

        html = util.html_get(uri)
        forecast = self.forecast_get(html)

        datas = re.findall(r'"x":([0-9]+),"y":([0-9.]+),"description":"([higlow]+)"', forecast)

        for data in datas:
            list_data = list(data)
            list_data[0] = int(list_data[0])
            self.tides.append(list_data)
    
    def get(self, start=0, end=3600*24*365*100000):
        result = []
        for tide in self.tides:
            if tide[0] >= start and tide[0] < end:
                result.append(tide)
        return result

    def print(self, start=0, end=3600*24*365*100000):
        results = self.get(start, end)
        print ("tide: ", end="")
        for result in results:
            if result[2]=='high':
                highlow = "H"
            else:
                highlow = "L"
            ts = time.gmtime(result[0])
            print("{}-{}".format(highlow, time.strftime("%H:%M ", ts)), end=' ')
        print("")

if __name__ == "__main__":
    tide = Tide("https://tides.willyweather.com.au/nsw/sydney/south-head.html")
    tide.print()