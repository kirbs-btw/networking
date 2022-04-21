import socket
import threading
from encrypt import *
from decrypt import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.178.37', 55555))

user_name = input("USER: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(decrypt(message))
        except:
            print("something went wrong!")
            client.close()
            break

def write():
    while True:
        message = encrypt(f"{user_name}: {input('')}").encode('ascii')
        client.send(message)

revice_thread = threading.Thread(target=receive)
revice_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()