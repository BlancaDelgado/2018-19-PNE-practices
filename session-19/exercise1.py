# Program for analyzing Chuck Norris in API

import http.client
import json
import sys
import termcolor

def connect(ENDPOINT):

    HOSTNAME = 'api.icndb.com'
    METHOD = 'GET'

    termcolor.cprint('Connecting: http://' + HOSTNAME + ENDPOINT, 'green')
    conn = http.client.HTTPConnection(HOSTNAME)  # connect
    conn.request(METHOD, ENDPOINT)  # send request

    r = conn.getresponse()
    termcolor.cprint('Response received: {num} {OK}'.format(num=r.status, OK=r.reason), 'green')
    print()

    txt_json = r.read().decode('utf-8')
    data = json.loads(txt_json)
    conn.close()

    return data


# OBTAINING INFO
try:
    r_num_jokes = connect('/jokes/count')
    r_categories = connect('/categories')
    r_joke = connect('/jokes/random')
except KeyboardInterrupt:
    sys.exit()


# -- main

n = 11  # title
print('\n', '-'*n, 'CHUCK NORRIS', '-'*n, '\n')


# 1.- NUMBER OF TOTAL JOKES IN DATABASE
num_jokes = r_num_jokes['value']
print('· Total number of jokes:', num_jokes)

# 2.- NUMBER AND NAMES OF ALL CATEGORIES
list_categories = r_categories['value']
num_categories = len(list_categories)
str_categories = ', '.join(list_categories)
print('· Total number of categories:', num_categories)
print()
print('· CATEGORIES:', str_categories)

# 3.- RANDOM JOKE
joke = r_joke['value']['joke']
print('· JOKE:', joke)
