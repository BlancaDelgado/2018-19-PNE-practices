# Try chatting with my partners

import socket

# CREATE SOCKET
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8081
IP = "212.128.253.75"

# CONNECT TO SERVER
s.connect((IP, PORT))

# INTERACT WITH SERVER
s.send(str.encode('Hello baby.'))
msg = s.recv(2048).decode('utf-8')
print('>>', msg)

# CLOSE SOCKET
s.close()

