# Programming our first client.

import socket

# CREATE A SOCKET FOR COMMUNICATING WITH SERVER
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket created.')

PORT = 8082
IP = '212.128.253.64'

# CONNECT TO SERVER
s.connect((IP, PORT))

# SEND MESSAGE TO SERVER (CONVERT STRING TO BITES)
s.send(str.encode('HELLO FROM MY CLIENT'))

# RECEIVE MESSAGE FROM SERVER (ALWAYS IN BITES!)
msg = s.recv(2048).decode('utf-8') # (max. size of message to receive)
print('MESSAGE FROM SERVER:')
print(msg)

# CLOSE SOCKET
s.close()

print('The end')
