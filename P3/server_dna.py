# Server for performing operations on a sequence: total length, number and percentage of a base.

import socket  # allow client-server connection
from P1.Seq import Seq  # access class with sequence functions

def process(cs):
    """
    Processes the message from the client

    :param cs: client socket
    :return: list with all client requests (DNA sequence and commands)
    """
    msg = cs.recv(2048).decode('utf-8')  # obtain message from client
    msg_list = msg.split('\n')  # make a list of the message with all requests
    return msg_list


def attend_seq(req):

    # FIRST LINE
    # - ALIVE: request is blank
    # - ERROR: sequence is not valid (!= A,C,G,T, BUT they can be lower)
    # - OK: the sequence is valid

    # OBTAIN SEQUENCE
    seq = str(req[0])

    # IF SEQUENCE IS EMPTY...
    if seq == False:
        return 'ALIVE!'

    # IF SEQUENCE IS NOT EMPTY...
    values = []  # check what values make the sequence

    for i in seq:
        if i not in values:
            values.append(i)

    if values in 'ACGT':
        return 'OK'

    else:
        return 'ERROR'


IP = '127.0.0.1'
PORT = 8080

MAX_OPEN_REQUESTS = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket
s.bind((IP, PORT))  # bind to desired location
s.listen(MAX_OPEN_REQUESTS)  # set maximum number of clients

print('Server socket ready: {}'.format(s))  # everything OK?

while True:  # connect to clients
    print('Waiting for connections at: {}, {}'.format(IP, PORT))  # wait for clients

    (clientsocket, address) = s.accept()  # accept connections from client sockets
    print('Attending client: {}'.format(address))  # attend the client now

    requests = process(clientsocket)  # get the information of the client
    check_seq = attend_seq(requests)  # check if the seq is alright (ALIVE!, OK, ERROR)
    print(check_seq)

    try_msg = 'hi'
    clientsocket.send(str.encode(try_msg))  # send message

    clientsocket.close()  # close socket


# --MESSAGE FROM SERVER



# FOLLOWING LINES
# Corresponding to the lines in the client
