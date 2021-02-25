import re
import weather_util as util
import time

class Seatempnet:
    def forecast_get(self, html):
        split_htmls = html.split('\n')

        for split_html in split_htmls:
            if split_html.find('CURRENT SEA TEMPERATURE') != -1:
                return split_html

    def time_get(self):
        return util.time_get(time.strftime("%Y-%m-%d"))

    def __init__(self, uri):
        # self.seatemps = []
        # html = util.html_get(uri)
        # forecast_seatemp = self.forecast_get(html)
        # print(forecast_seatemp)
        # m = re.match(r".+<b>([0-9.]+)</b>", forecast_seatemp)
        # print(m)
        # self.temp = m.group(1)
        self.temp = "23.2" 
        
    def get(self, start=0, end=3600*24*365*100000):
        self.temp

    def print(self, start=0, end=3600*24*365*100000):
        print("sea-temperature: {}°C".format(self.temp))

def test():
    sample = "<h3>CURRENT SEA TEMPERATURE</h3><p><b>Nelson Bay (Australia)</b></p><h2><b>18.5</b><small><sup>o</sup>C</small></h2><p>Data updated<br><b>August 2 at 11:41</b></p><div class='propusk10'></div><p>Water temperature yesterday:</p><h4>18.8</big></b><small><sup>o</sup>C</small></h4><div class='propusk10'></div><p>The range of possible temperatures in August:</p><h4>17.4</big></b><small><sup>o</sup>C</small> / 20.5</big></b><small><sup>o</sup>C</small></h4> </div>"
    m = re.match(r".+<b>([0-9.]+)</b>", sample)
    print(m.group(1))
if __name__ == "__main__":
    test()
    # seatemp = Seatempnet(r"http://seatemperature.net/current/australia/nelson-bay-new-south-wales-australia-sea-temperature")
    # seatemp.print()
    # seatemp = Seatemp(r"https://www.seatemperature.org/australia-pacific/australia/sydney.htm")
    # seatemp.print()
    # seatemp = Seatemp(r"https://www.seatemperature.org/australia-pacific/australia/sydney.htm")
    # seatemp.print()
    # seatemp = Seatemp(r"https://www.seatemperature.org/australia-pacific/australia/dee-why.htm")
    # seatemp.print()
    # seatemp = Seatemp(r"https://www.seatemperature.org/australia-pacific/australia/nelson-bay.htm")
    # seatemp.print()
