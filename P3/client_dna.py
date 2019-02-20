# Client that asks for information for DNA sequences

import socket  # allow client-server connection


def get_msg():
    """
    Gets DNA sequence and all commands (that will be sent to server)

    -- POSSIBLE OPTIONS FOR FIRST LINE
    empty: used to check if server is ok
    not empty: sequence of DNA

    -- POSSIBLE COMMANDS IN FOLLOWING LINES
    len: calculate the sequence length
    complement: calculate complement
    reverse: calculate reverse
    countA: calculate number of bases (same for T, G, C)
    percA: calculate percentage of A bases (same for T, G, C)

    :return: seq and commands separated by < \n >
    """
    # FIRST LINE
    seq = input('Enter your sequence (leave blank to check server): ').upper()

    # FOLLOWING LINES
    new_command = True  # allow to start loop
    full_command = ''  # define variable

    no_ans = ['']
    characteristics = ['len', 'complement', 'reverse']
    counts = ['countA', 'countC', 'countG', 'countT']
    percs = ['percA', 'percC', 'percG', 'percT']
    options = no_ans + characteristics + counts + percs  # possibilities for the answers

    while new_command:
        new_command = input('Enter a command (press ENTER when finished): ').lower()

        if new_command in options:
            full_command += '\n' + new_command

        else:
            print('ERROR: Please introduce a valid option ({}'.format(options) + ')!')

    msg = seq + full_command
    return msg


def interact(msg, location):
    """
    Client interacts with server: sending and receiving messages
    :param msg: message from client
    :param location: tuple (IP, PORT)
    :return: response from server
    """
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket
        s.connect(location)  # connect socket
        s.send(str.encode(msg))  # send message
        resp = s.recv(2048).decode()  # receive message
        s.close()  # finally, close socket

        return resp


def main():
    """
    Main program.
    :return: None
    """

    # OBTAIN MESSAGE
    c_msg = get_msg()

    # INTERACT WITH SERVER
    ip = '127.0.0.1'
    port = 8080
    location = (ip, port)

    s_msg = interact(c_msg, location)
    print(s_msg)
    return


try:
    main()
except KeyboardInterrupt:
    exit()
