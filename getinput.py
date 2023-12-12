import requests
from http import cookiejar
import inspect
import re

cookie = cookiejar.MozillaCookieJar()
cookie.load('cookies.txt')

"""
automatically detects if any file in the callstack is of the form day$i.py where $i is a number,
then gets the input for that number day of the 2023 advent. if no file is, it will return None
"""
def fetch():
    for s in inspect.stack():
        m = re.search(r'/day(\d+)\.py', s.filename)
        if m:
            i = m[1]
            break
    else:
        return None
    return requests.get(f'https://adventofcode.com/2023/day/{i}/input', cookies=cookie).text


def fetchlines():
    return fetch().strip().split('\n')