# Analysing the weather of capitals

import sys
import http.client
import json
import termcolor


def connect(ENDPOINT, woeid):

    HOSTNAME = 'www.metaweather.com'
    METHOD = "GET"

    termcolor.cprint('Connecting: http://' + HOSTNAME + ENDPOINT + woeid + '/')
    conn = http.client.HTTPSConnection(HOSTNAME)
    conn.request = (METHOD, ENDPOINT + woeid + '/')

    r = conn.getresponse()
    termcolor.cprint('Response received {num} {OK}'.format(num=r.status, OK=r.reason))

    txt_json = r.read().decode('utf-8')
    data = json.load(txt_json)

    conn.close()

    return data






# FIND WOEID OF CITY


# ERROR IF NOT FOUND




# 1.- ASK FOR CAPITAL

capital = input('Introduce location: ')


# 2.- PRINT INFO (TIME, TEMP, SUNSET)
