import tkinter as tk
import socket
import threading

def send_message(event=None):
    message = message_entry.get()
    if message:
        chat_log.insert(tk.END, f'You: {message}\n')
        client.send(message.encode('utf-8'))
        message_entry.delete(0, tk.END)

def receive_message():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            chat_log.insert(tk.END, f'Server: {message}\n')
        except ConnectionAbortedError:
            break

def on_closing():
    client.close()
    root.destroy()

def set_alias():
    alias = alias_entry.get()
    client.send(alias.encode('utf-8'))
    alias_entry.config(state=tk.DISABLED)
    set_alias_button.config(state=tk.DISABLED)

alias = ''
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 7007))

root = tk.Tk()
root.title('Chat Room Client')

alias_label = tk.Label(root, text='Enter your alias:',font=("Arial", 11))
alias_label.pack(pady=5)
alias_label.pack()

alias_entry = tk.Entry(root, width=40)
alias_entry.pack(pady=5)
alias_entry.pack()

set_alias_button = tk.Button(root, text='Set Alias', command=set_alias,
                         font = ("Arial", 12), bg = "purple", fg = "white", activebackground = "darkblue", padx = 10, pady = 5)
set_alias_button.pack(pady=12)
set_alias_button.pack()

chat_log = tk.Text(root, width=50, height=20)
chat_log.pack()

message_entry = tk.Entry(root, width=60)
message_entry.pack(pady=12)
message_entry.pack()
message_entry.bind("<Return>", send_message)

send_button = tk.Button(root, text='Send', command=send_message,
                        font = ("Arial", 12), bg = "purple", fg = "white", activebackground = "darkblue", padx = 10, pady = 5)
send_button.pack(pady=12)
send_button.pack()

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()



###########################################################################

# import tkinter as tk
# import socket
# import threading
#
# def receive_messages():
#     while True:
#         try:
#             message = client.recv(1024).decode('utf-8')
#             chat_log.insert(tk.END, f'Them: {message}\n')
#         except ConnectionAbortedError:
#             break
#
# def send_message(event=None):
#     message = message_entry.get()
#     if message:
#         client.send(message.encode('utf-8'))
#         chat_log.insert(tk.END, f'You: {message}\n')
#         message_entry.delete(0, tk.END)
#
# def on_closing():
#     client.close()
#     root.destroy()
#
# def set_alias():
#     global alias
#     alias = alias_entry.get()
#     client.send(alias.encode('utf-8'))
#     alias_entry.config(state=tk.DISABLED)
#     set_alias_button.config(state=tk.DISABLED)
#
# alias = ''
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('127.0.0.1', 7003))
#
# root = tk.Tk()
# root.title('Chat Room Client')
#
# alias_label = tk.Label(root, text='Enter your alias:')
# alias_label.pack()
#
# alias_entry = tk.Entry(root)
# alias_entry.pack()
#
# set_alias_button = tk.Button(root, text='Set Alias', command=set_alias)
# set_alias_button.pack()
#
# chat_log = tk.Text(root, width=50, height=20)
# chat_log.pack()
#
# message_entry = tk.Entry(root, width=50)
# message_entry.pack()
# message_entry.bind("<Return>", send_message)
#
# send_button = tk.Button(root, text='Send', command=send_message)
# send_button.pack()
#
# receive_thread = threading.Thread(target=receive_messages)
# receive_thread.start()
#
# root.protocol("WM_DELETE_WINDOW", on_closing)
# root.mainloop()

