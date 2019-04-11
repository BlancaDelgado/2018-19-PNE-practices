# Accessing GITHUB

import http.client
import json
import termcolor
import sys


def connect(ENDPOINT):
    """
    Client that connects to GITHUB.
    :param ENDPOINT: request to obtain desired info.
    :return: json file downloaded from GITHUB.
    """

    HOSTNAME = "api.github.com"
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


try:

    while True:
        # ASK FOR USERNAME
        GITHUB_ID = input('GITHUB ID: ')

        e_github = "/users/" + GITHUB_ID
        d_github = connect(e_github)

        # Check if username exists
        if 'login' in d_github.keys():

            # Real name
            name = d_github['name']

            # Names of repos
            e_repos = "/users/" + GITHUB_ID + "/repos"
            d_repos = connect(e_repos)



            # PRINT ALL INFO
            n = 16
            print('\n', '-'*n, 'GITHUB', '-'*n)
            print('· Real name:', name)

            print('\n· Repositories:')
            num = 0
            for repo in d_repos:
                r_name = repo['name']

                if r_name == '2018-19-PNE-practice':
                    # Number of contributions
                    e_commits = "/repos/" + GITHUB_ID + "/" + r_name + "/contributors"
                    d_commits = connect(e_commits)
                    print()

                    commits = d_commits[0]['contributions']

                else:
                    commits = '?'

                print('\tRepository', num+1, '-', r_name, '({commits} commits)\n'.format(commits=commits))

        else:
            print('ERROR: that username does not exist.\n')


except KeyboardInterrupt:
    sys.exit('\nEXIT BY USER.')
