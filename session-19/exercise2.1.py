# Weather of capitals

import termcolor
import http.client
import json

HOSTNAME = "www.metaweather.com"

city = input('Introduce capital:').lower()

ENDPOINT = "/api/location/search/?query=" + city

METHOD = "GET"
headers = {'User-Agent': 'http-client'}

termcolor.cprint('Connecting: ' + 'http://' + HOSTNAME + ENDPOINT, 'green')
conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT, None, headers)

r = conn.getresponse()

termcolor.cprint('Response received: {num} {OK}'.format(num=r.status, OK=r.reason), 'green')

txt_json = r.read().decode("utf-8")
conn.close()

data = json.loads(txt_json)


print(data)
