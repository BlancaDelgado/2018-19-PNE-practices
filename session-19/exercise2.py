# Weather of capitals

import termcolor
import http.client
import json

termcolor.cprint('Hello', 'blue')

HOSTNAME = "www.metaweather.com"

city = input('Introduce capital:').lower()

ENDPOINT = "/api/location/search/?query=" + city

METHOD = "GET"
headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT, None, headers)

r = conn.getresponse()

print('Response received {num} {OK}'.format(num=r.status, OK=r.reason))

txt_json = r.read().decode("utf-8")
conn.close()

print(txt_json)
