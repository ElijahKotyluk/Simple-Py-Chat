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
''' ln27: Store clients address in dictionary, then starts the handling thread for that client. '''
def accept_incoming_connections():
    ''' Handle incoming requests from clients '''
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Welcome to the underground." +
        "Type your screen name and press enter.",
        "utf8"))
        addresses[client] = client_addressThread(target=handle_client, args=(client,)).start()

''' Takes client socket as arg. '''
def handle_client(client):
    ''' Handles single client connection. '''
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you want to quit, type {quit} to exit.' % name
    client.send(bytes,(msg, "utf8"))
    msg = "%s has joined the chat." % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name
    while True:
        msg = client.recv[BUFSIZ]
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break