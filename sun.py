import time
import re
import weather_util as util

class Sun:   
    def forecast_get(self, html):
        return html

    def __init__(self, uri):
        self.suns = []

        html = util.html_get(uri)

        forecast = self.forecast_get(html)
        datas = re.findall(r'"x":([0-9]+),"description":"([A-Za-z ]+)"', forecast)
        for data in datas:
            list_data = list(data)
            list_data[0] = int(list_data[0])
            self.suns.append(list_data)

    def get(self, start=0, end=3600*24*365*100000):
        result = []
        for sun in self.suns:
            if sun[0] >= start and sun[0] < end:
                result.append(sun)
        return result

    def print(self, start=0, end=3600*24*365*100000):
        results = self.get(start, end)
        print ("sun: ", end="")
        for result in results:
            ts = time.gmtime(result[0])
            print(time.strftime("%H:%M ", ts), end=' ')
        print("")

if __name__ == "__main__":
    sun = Sun(r"https://sunrisesunset.willyweather.com.au/nsw/sydney/south-head.html")
    sun.print()
