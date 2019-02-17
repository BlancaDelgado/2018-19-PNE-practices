# Try chatting on my own

import socket

# CREATE SOCKET
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8080
IP = '10.0.2.15'

# CONNECT TO SERVER
s.connect((IP, PORT))

# INTERACT WITH SERVER
s.send(str.encode('Hello baby.'))
msg = s.recv(2048).decode('utf-8')
print('>>', msg)

# CLOSE SOCKET
s.close()
