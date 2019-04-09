# Analysing the weather of capitals

import sys
import http.client
import json
import termcolor


def connect(ENDPOINT):
    """
    Connects to metaweather and obtains response depending on the ENDPOINT requested.
    :param ENDPOINT: web address to request specific operations.
    :return: json file with requested information.
    """

    # define all variables
    HOSTNAME = 'www.metaweather.com'
    METHOD = "GET"

    headers = {'User-Agent': 'http-client'}

    # CONNECT
    termcolor.cprint('Loading: http://' + HOSTNAME + ENDPOINT, 'green')
    conn = http.client.HTTPSConnection(HOSTNAME)
    conn.request = (METHOD, ENDPOINT, None, headers)

    r = conn.getresponse()
    txt_json = r.read().decode("utf-8")
    data = json.load(txt_json)

    termcolor.cprint('Response received {num} {OK}'.format(num=r.status, OK=r.reason), 'green')
    return data


def get_woeid(city):

    endpoint = '/api/location/search/?query='+city
    data = connect(endpoint)

    # ELABORATED RESPONSE
    if data:
        print('Data:', data)
        city_woeid = data[0]['woeid']

    else:
        city_woeid = False
        print('ERROR: this city is not in the data base.\n')

    return city_woeid


# -- Main program

n = 8
print('-'*n + ' WEATHER ' + '-'*n)
try:

    while True:

        # 1.- ASK FOR CAPITAL
        capital = input('Introduce location: ').lower()

        # Find woeid of city
        woeid = get_woeid(capital)

        # 2.- PRINT INFO

        # Time

        # Temperature

        # Sunset



except KeyboardInterrupt:
    sys.exit('EXIT BY USER.')
