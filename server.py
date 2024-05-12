import tkinter as tk
import socket
import threading


def receive_messages():
    global client
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            text.insert(tk.END, f'{alias}: {message}\n')
        except ConnectionAbortedError:
            break

def send_message(event=None):
    global client
    message = message_entry.get()
    client.send(message.encode('utf-8'))
    text.insert(tk.END, f'You: {message}\n')
    message_entry.delete(0, tk.END)

def on_closing():
    global client
    client.close()
    root.destroy()

host = '127.0.0.1'
port = 7007

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
client, address = server.accept()

alias = client.recv(1024).decode('utf-8')
print(f'The alias of this client is {alias}')

root = tk.Tk()
root.title('Server')

text = tk.Text(root, height=20, width=50)
text.pack()

message_entry = tk.Entry(root, width=50)
message_entry.pack()
message_entry.bind("<Return>", send_message)

send_button = tk.Button(root, text='Send', command=send_message,
                        font=("Arial", 12), bg="purple", fg="white", activebackground="darkblue", padx=10, pady=5)
send_button.pack(pady=12)
send_button.pack()

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()




#################################################################################

# import socket
#
# host = '127.0.0.1'
# port = 7003 # Use a different port number
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((host, port))
# server.listen(1)  # Listen for only one client
#
# print('Server is running and listening ...')
#
# client, address = server.accept()
# print(f'Connection is established with {str(address)}')
#
# alias = client.recv(1024).decode('utf-8')
# print(f'The alias of this client is {alias}')
#
# while True:
#     message = client.recv(1024).decode('utf-8')
#     print(f'{alias}: {message}')
#     reply = input('Your message: ')
#     client.send(reply.encode('utf-8'))

































