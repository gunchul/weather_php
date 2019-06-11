import re
import weather_util as util
import time

class Seatemp:
    def forecast_get(self, html):
        split_htmls = html.split('\n')

        for i, split_html in enumerate(split_htmls):
            if split_html.find('id="sea-temperature') != -1:
                return split_htmls[i+1]

    def time_get(self):
        return util.time_get(time.strftime("%Y-%m-%d"))

    def __init__(self, uri):
        self.seatemps = []
        html = util.html_get(uri)
        forecast_seatemp = self.forecast_get(html)

        temperatures = list(re.findall(r'([0-9.]+)', forecast_seatemp))
        
        self.seatemps.append([self.time_get(), temperatures[0]])
        
    def get(self, start=0, end=3600*24*365*100000):
        result = []
        for seatemp in self.seatemps:
            if seatemp[0] >= start and seatemp[0] < end:
                result.append(seatemp)
        return result

    def print(self, start=0, end=3600*24*365*100000):
        results = self.get(start, end)
        for result in results:
            print ("sea-temperature: {}°C".format(result[1]))

if __name__ == "__main__":
    seatemp = Seatemp(r"https://www.seatemperature.org/australia-pacific/australia/newcastle.htm")
    seatemp.print()