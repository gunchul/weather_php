import re
import requests
import time

def html_get(uri):
    s = re.search(r"^http", uri)
    if s:
        r = requests.get(uri)
        result = r.content.decode("utf-8")
    else:
        f = open(uri)
        html = f.read()
        f.close()
        result = html
    return result

def time_get(time_str):
    t = time.mktime(time.strptime(time_str, "%Y-%m-%d"))
    return t - time.altzone
