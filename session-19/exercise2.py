# Weather of capitals

import termcolor
import http.client
import json
import sys


def connect(ENDPOINT):
    """
    Client that connects to metaweather.
    :param ENDPOINT: request to obtain desired info.
    :return: json file downloaded from metaweather.
    """

    HOSTNAME = "www.metaweather.com"
    METHOD = "GET"
    headers = {'User-Agent': 'http-client'}

    # CONNECT
    termcolor.cprint('\nConnecting: ' + 'http://' + HOSTNAME + ENDPOINT, 'green')
    conn = http.client.HTTPSConnection(HOSTNAME)
    conn.request(METHOD, ENDPOINT, None, headers)
    r = conn.getresponse()

    # POLISH INFO
    termcolor.cprint('Response received: {num} {OK}'.format(num=r.status, OK=r.reason), 'green')
    txt_json = r.read().decode("utf-8")
    conn.close()

    data = json.loads(txt_json)
    return data


# -- main program

n = 11  # print title
print('-'*n + ' THE WEATHER ' + '-'*n)

try:
    while True:
        # 1.- ASK FOR CITY
        city = input('\nIntroduce capital: ').lower()

        e_location = "/api/location/search/?query=" + city
        d_location = connect(e_location)

        # 2.- OBTAIN INFO
        if d_location:  # if there is data of city
            woeid = d_location[0]['woeid']

            # FORECAST
            e_forecast = "/api/location/" + str(woeid) + "/"
            d_forecast = connect(e_forecast)

            title = d_location[0]['title'].upper()
            print('\nFORECAST FOR ', title)

            # Local time
            complex_time = d_forecast['time'].split('T')[1]
            time = complex_time.split('.')[0]
            print('· Local time:', time)

            # Temperature
            temp = d_forecast['consolidated_weather'][0]['the_temp']
            temp = str(round(temp, 2)) + 'ºC'
            print('· Temperature:', temp)

            # Sunset
            complex_sunset = d_forecast['sun_set'].split('T')[1]
            sunset = complex_sunset.split('.')[0]
            print('· Sunset at:', sunset)

        else:  # if there is no data about location
            print('ERROR: this city is not registered.')

except KeyboardInterrupt:
    sys.exit('\nEXIT BY USER.')
