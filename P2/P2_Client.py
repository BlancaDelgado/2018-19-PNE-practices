# Practice 2 client-server program that:
# - Asks user for a sequence
# - Calculates reverse-complement using Seq Class
# - Sends string to server
# - Repeat the process in a loop
# - Verify that client works examining Server's console


# IMPORT CLASS SEQ (to obtain sequences)
from P1.Seq import Seq

# IMPORT SOCKET (to create chat)
import socket

# OBTAIN SEQUENCE
seq = True
while seq:
    seq = input('Introduce a sequence (print exit to stop): ').upper()

    # STOP THE PROGRAM IF EXIT
    if seq == 'EXIT':
        seq = False

    else:
        # CALCULATE REVERSE-COMPLEMENT SEQUENCE
        reverse = Seq(seq).reverse()  # calculate sequence

        # SEND MESSAGE
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # open socket

        PORT = 8081  # define location
        IP = '10.0.2.15'

        s.connect((IP, PORT))  # connect
        s.send(str.encode(reverse))  # send

        # CHECK EVERYTHING IS ALRIGHT
        msg = s.recv(2000).decode('utf-8')
        print(msg)

        # CLOSE SOCKET
        s.close()
