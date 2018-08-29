from socket import AF_INET, sockert, SOCK_STREAM
from threading import thread
import tkinter

''' Handle received messages. '''
def receive():
    while True:
        try: msg = client_socket.recv(BUFSIZ).decode("utf8") # Wait for message to be received.
        msg_list.insert(tkinter.END, msg) # Append message to msg_list.
    except OSError: # Client leaves chat.
        break

def send(event=None): # Event passed by binders.
    msg = my_msg.get() # Extract message being sent.
    my_msg.set("") # Clear msg field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}": # Close client_socket if user input is {quit}
        client_socket.close()
        top.quit()

def on_closing(event=None):
    my_msg.set("{quit}")
    send()

top tkinter.Tk() # Create frame for chat box.
top.title("Chat")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar() # To send messages
my_msg.set("Type messages here.")
scrollbar = tkinter.Scrollbar(messages_frame) # Navigate through past conversation.

msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, filler=tkinter.BOTH)
msg_list.pack()

messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

HOST = input('Enter host: ')
PORT = input('Enter port; ')

BUFSIZ = 1024
ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()