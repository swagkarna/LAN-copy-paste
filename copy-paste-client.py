#!/bin/python

import requests
import sys
from bs4 import BeautifulSoup

url = 'http://localhost:6664/'
headers = {
    'Host': '192.168.82.103:6664',
    'Proxy-Connection': 'keep-alive',
    'Content-Length': '33',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://192.168.82.103:6664',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://192.168.82.103:6664/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
}

if len(sys.argv) == 1:
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        print soup.find('textarea').get_text()
else:
        data = 'text=' + sys.argv[1] +'%21&my-form=Upload+Text'
