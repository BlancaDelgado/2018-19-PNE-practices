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
    if not seq:
        return 'ALIVE!'  # try server

    # IF SEQUENCE IS NOT EMPTY...
    values = 'ACGT'

    for i in seq:
        if i not in values:
            return 'ERROR'# values DON'T match


    return 'OK'  # no errors where found


def attend_com(req, com):
    """
    Obtains answer from Seq class according to the command

    len: calculate the sequence length
    complement: calculate complement
    reverse: calculate reverse
    countA: calculate number of bases (same for T, G, C)
    percA: calculate percentage of A bases (same for T, G, C)

    :param req: list with sequence and series of commands
    :param com: command to be analyzed
    :return: information from Seq (matching with command)
    """

    operation = Seq(req[0])

    if com == 'len':
        return operation.len()
    elif com == 'complement':
        return operation.complement()
    elif com == 'reverse':
        return operation.reverse()
    elif 'count' in com:
        for i in 'ACGT':
            if i in com:
                return operation.count(i)
    elif 'perc' in com:
        for i in 'ACGT':
            if i in com:
                return operation.perc(i)


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

    # GET MESSAGE
    requests = process(clientsocket)  # get the information of the client

    # FIRST LINE
    answer = attend_seq(requests)  # check if the seq is alright (ALIVE!, OK, ERROR)

    # FOLLOWING LINES
    if answer == 'OK':

        for command in requests[1:]:
            answer += '\n'
            answer += str(attend_com(requests, command))

    # SEND MESSAGE
    clientsocket.send(str.encode(answer))

    clientsocket.close()  # close socket
