import time
import re
import weather_util as util
import swell
import wind

class SwellWind:
    def merge(self, swells, winds):
        for swell in swells:
            for wind in winds:
                if swell[0] == wind[0]:
                    for w in wind[1:]:
                        swell.append(w)
                    self.swell_winds.append(swell)

    def __init__(self, swells, winds):
        self.swell_winds = []
        self.merge(swells, winds)

    def get(self, start=0, end=3600*24*365*100000):
        result = []
        for swell_wind in self.swell_winds:
            if swell_wind[0] >= start and swell_wind[0] < end:
                result.append(swell_wind)
        return result

    def print(self, start=0, end=3600*24*365*100000):
        results = self.get(start, end)
        print ("<----   Swell   ----> | <---- Wind ---->")
        for result in results:
            ts = time.gmtime(result[0])
            print("{}: {}m, {}s, {} | {}km/h, {}".format(time.strftime("%H:%M", ts), result[1], result[3], result[2], result[4], result[5]))

if __name__ == "__main__":
    swelli = swell.Swell(r"https://swell.willyweather.com.au/nsw/sydney/south-head.html")
    windi = wind.Wind(r"https://wind.willyweather.com.au/nsw/sydney/south-head.html")

    swell_wind = SwellWind(swelli.get(), windi.get())
    swell_wind.print()
