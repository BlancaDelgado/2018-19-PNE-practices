# Analysing the weather of capitals

import sys
import http.client
import json
import termcolor


# -- Main program

n = 8
print('-'*n + ' WEATHER ' + '-'*n)
try:



    # 1.- ASK FOR CAPITAL
    city = input('Introduce location: ')
    city = city.lower()

    # 2.- FIND WOEID OF CITY

    # define variables for connection
    ENDPOINT = '/api/location/search/?query=' + city

    HOSTNAME = "www.metaweather.com"
    METHOD = "GET"

    headers = {'User-Agent': 'http-client'}

    # CONNECT
    termcolor.cprint('Loading: http://' + HOSTNAME + ENDPOINT, 'green')
    conn = http.client.HTTPSConnection(HOSTNAME)
    conn.request = (METHOD, ENDPOINT, None, headers)

    r = conn.getresponse()
    txt_json = r.read().decode("utf-8")
    conn.close()

    data = json.load(txt_json)

    termcolor.cprint('Response received {num} {OK}'.format(num=r.status, OK=r.reason), 'green')

    # ELABORATED RESPONSE
    if data:
        print('Data:', data)
        city_woeid = data[0]['woeid']

    else:
        city_woeid = False
        print('ERROR: this city is not in the data base.\n')


    print(city_woeid)
    # 2.- PRINT INFO

    # Time

    # Temperature

    # Sunset



except KeyboardInterrupt:
    sys.exit('EXIT BY USER.')
