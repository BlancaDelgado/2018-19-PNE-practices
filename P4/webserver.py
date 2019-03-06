# Web server with index and access to blue, pink and error.

import socket  # allow communication
import termcolor  # allow terminal colors

# BASIC CONFIGURATIONS

IP = '127.0.0.1'
PORT = 8081

MAX_OPEN_REQUESTS = 5


def process(client_socket):

    request = client_socket.recv(2048).decode('utf-8')

    if request:
        termcolor.cprint(('\nREQUEST MESSAGE: \n' + request), 'green')

    if ' ' in request:  # avoid errors
        line_commands = request.split(' ')
        resource = line_commands[1]

        # PAGE OPTIONS
        if resource == '/':
            filename = 'index.html'

        elif resource == '/blue':
            filename = 'blue.html'

        elif resource == '/pink':
            filename = 'pink.html'

        else:
            filename = 'error.html'

        # OPEN CORRECT PAGE
        with open(filename, 'r') as file:
            content = file.read()
            file.close()

        status_line = 'HTTP/1.1 200 OK \r\n'
        header = 'Content-Type: text/html \r\n'
        header += 'Content-Length: {}\r\n'.format(len(str.encode(content)))

        response = status_line + header + content
        client_socket.send(str.encode(response))

        client_socket.close()

    return


# -- main program

# SERVER SOCKET: CREATE, BIND, CONFIGURE (LISTEN)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(MAX_OPEN_REQUESTS)

print('...socket ready: {}'.format(server))

# INTERACT WITH CLIENTS: ACCEPT, ATTEND
while True:
    print('...waiting for connections at: {}, {}'.format(IP, PORT))
    (client, address) = server.accept()

    print('...attending connections from client: {}'.format(address))
    process(client)
