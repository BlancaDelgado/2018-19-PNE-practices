# My first server

import socket

PORT = 8080
IP = '212.128.253.97'
MAX_OPEN_REQUEST = 5


def process_client(cs):
    """
    Function specialized for attending the requests of the client.
    Reading message from client and sending it back.

    :param cs: client socket
    :return: None
    """

    # RECEIVE AND PRINT MESSAGE
    msg = cs.recv(2048).decode('utf-8')
    print('>>> {}'.format(msg))

    # SEND MESSAGE BACK TO CLIENT (ECO-SERVER)
    cs.send(str.encode(msg))

    return


# CREATE A SOCKET FOR CONNECTING TO THE CLIENTS
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket connecting through internet
# type stream for writing and reading

# BIND SOCKET TO DESIRED LOCATION
serversocket.bind((IP, PORT))  # one parameter with two pieces of info

# CHOOSE AMOUNT OF POSSIBLE CLIENTS
serversocket.listen(MAX_OPEN_REQUEST)

# CHECK EVERYTHING IS ALRIGHT
print('Socket ready: {}'.format(serversocket))


while True:
    # CONNECT TO CLIENTS
    print('Waiting for connections at: {}, {}'.format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # PROCESS THE CLIENT
    print('Attending client: {}'.format(address))
    process_client(clientsocket)

    # CLOSE THE SOCKET
    clientsocket.close()
