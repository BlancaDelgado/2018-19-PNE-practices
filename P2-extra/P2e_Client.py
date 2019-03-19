# Client that asks for sequence and sends it to server, to return complement.

import socket

seq = True
while seq:
    seq = input('Introduce a sequence (print exit to stop): ').upper()

    # STOP THE PROGRAM IF EXIT
    if seq == 'EXIT':
        seq = False

    else:
        # SEND MESSAGE
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # open socket

        PORT = 8082  # define location
        IP = '10.0.2.15'

        s.connect((IP, PORT))  # connect
        s.send(str.encode(seq))  # send

        # RECEIVE COMPLEMENT SEQUENCE
        msg = s.recv(2000).decode('utf-8')
        print('Complement sequence: ' + msg + '\n')

        # CLOSE SOCKET
        s.close()
