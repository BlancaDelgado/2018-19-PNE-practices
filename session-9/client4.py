# Fixed client from github that does not block server.

# DO NOT CONNECT TO THE SERVER UNTIL ALL INFORMATION IS ADQUIRED!

import socket

# SERVER IP, PORT
IP = '212.128.253.97'
PORT = 8082


while True:
    # The client is not blocking the server.... 
    msg = input("> ")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers response
    response = s.recv(2048).decode()

    s.close()

    # Print the server's response
    print("Response: {}".format(response))
