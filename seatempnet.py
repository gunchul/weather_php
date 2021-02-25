import re
import weather_util as util
import time
from bs4 import BeautifulSoup

class Seatempnet:
    def time_get(self):
        return util.time_get(time.strftime("%Y-%m-%d"))

    def __init__(self, uri):
        self.seatemps = []
        html = util.html_get(uri)
        soup = BeautifulSoup(html, 'html.parser')
        templine = str(soup.find(id='temp1'))
        m = re.search("<h3>([0-9.]+)", templine)
        self.temp = m.group(1)
        
    def get(self, start=0, end=3600*24*365*100000):
        self.temp

    def print(self, start=0, end=3600*24*365*100000):
        print("sea-temperature: {}°C".format(self.temp))

def test():
    html = util.html_get(r"http://seatemperature.net/current/australia/nelson-bay-new-south-wales-australia-sea-temperature")
    soup = BeautifulSoup(html, 'html.parser')
    templine = str(soup.find(id='temp1'))
    print(templine)
    m = re.search("<h3>([0-9.]+)", templine)
    if m:
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
