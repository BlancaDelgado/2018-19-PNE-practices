# EXERCISE 2: Python client for implementing a chat (with loops).

import socket

send_msg = True
while send_msg != '\n':

    # CREATE SOCKET
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    PORT = 8081
    IP = '212.128.253.64'

    # CONNECT TO SERVER
    s.connect((IP, PORT))

    # INTERACT
    send_msg = input('Enter your message (press enter to stop):')
    s.send(str.encode(send_msg))

    receive_msg = s.recv(2048).decode('utf-8')
    print('\nMESSAGE FROM SERVER: ', receive_msg)

    # CLOSE SOCKET
    s.close()

print('The end.')