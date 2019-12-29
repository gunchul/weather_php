import time
import re
import sys
import datetime
import weather_util as util
import sun
import rain
import moon
import seatemp
import tide
import swell
import wind
import swell_wind

now = time.time()

willy = ".willyweather.com.au/nsw"

weather_type = {
    "sun":"sunrisesunset",
    "rain": "rainfall",
    "moon": "moonphases",
    "tide": "tides",
    "swell": "swell",
    "wind": "wind",
}

location_page = {
    "newcastle": "/hunter/newcastle-beach.html",
    "sydney": "/sydney/south-head.html",
    "wollongong": "/illawarra/wollongong-harbour.html",
    "frazer_beach": "/central-coast/frazer-beach.html",
    "boat_harbour": "/hunter/boat-harbour.html",
}

seatemp_page = {
    "newcastle": r"https://www.seatemperature.org/australia-pacific/australia/newcastle.htm",
    "sydney": r"https://www.seatemperature.org/australia-pacific/australia/sydney.htm",
    "wollongong": r"https://www.seatemperature.org/australia-pacific/australia/sydney.htm",
    "frazer_beach": r"https://www.seatemperature.org/australia-pacific/australia/dee-why.htm",
    "boat_harbour": r"https://www.seatemperature.org/australia-pacific/australia/nelson-bay.htm"
}



def willy_uri_get(type, location):
    return 'https://' + weather_type[type] + willy + location_page[location]

def date_str_get(secs):
    ts = time.localtime(secs)
    return time.strftime("%Y-%m-%d", ts), time.strftime("%a", ts)

def print_a_day(secs, sun, rain, moon, seatemp, tide, swell_wind):
    date_str, day_str = date_str_get(secs)
    start_secs = util.time_get(date_str)

    print(day_str, date_str)
    print("-------------------")

    if sun != None:
        sun.print(start_secs, start_secs + 3600*24)
    if rain != None:
        rain.print(start_secs, start_secs + 3600*24)
    if moon != None:
        moon.print(start_secs, start_secs + 3600*24)
    if seatemp != None:
        seatemp.print(start_secs, start_secs + 3600*24)
    if tide != None:
        tide.print(start_secs, start_secs + 3600*24)
    if swell_wind != None:
        swell_wind.print(start_secs, start_secs + 3600*24)
    print("")

location = "sydney"
locations = ["sydney", "newcastle", "wollongong", "frazer_beach", "boat_harbour"]
if len(sys.argv) >= 1 and sys.argv[1] in locations:
    location = sys.argv[1]

suni = sun.Sun(willy_uri_get("sun", location))
raini = rain.Rain(willy_uri_get("rain", location))
mooni = moon.Moon(willy_uri_get("moon", location))
seatempi = seatemp.Seatemp(seatemp_page[location])
tidei = tide.Tide(willy_uri_get("tide", location))
swelli = swell.Swell(willy_uri_get("swell", location))
windi = wind.Wind(willy_uri_get("wind", location))
swell_windi = swell_wind.SwellWind(swelli.get(), windi.get())

for i in range(0, 7):
    secs = now + 3600 * 24 * i
    print_a_day(secs, suni, raini, mooni, seatempi, tidei, swell_windi)   
