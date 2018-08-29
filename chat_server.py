from socket import AF_INET, socket, SOCK_STREAM
from threading import threading

clients = {}
addresses = {}

''' Specifies the socket is reachable by any address available by the machine '''
HOST = ''
PORT = 33000
''' Max size of input buffer '''
BUFSIZ = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
''' Bind socket address '''
SERVER.bind(ADDR)

''' While loop that waits for incoming connections, logs connection when successful. '''
def accept_incoming_connections():
    ''' Handle incoming requests from clients '''
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Welcome to the underground." +
        "Type your screen name and press enter.",
        "utf8"))
        addresses[client] = client_addressThread(target=handle_client, args=(client,)).start()