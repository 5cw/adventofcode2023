import requests
from http import cookiejar
import inspect
import re

cookie = cookiejar.MozillaCookieJar()
cookie.load('cookies.txt')


def fetch():
    for s in inspect.stack():
        m = re.search(r'/day(\d+)\.py', s.filename)
        if m:
            i = m[1]
            break
    else:
        i = None
    return requests.get(f'https://adventofcode.com/2023/day/{i}/input', cookies=cookie).text


def fetchlines():
    return fetch().strip().split('\n')