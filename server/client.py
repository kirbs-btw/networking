import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(message)
        except:
            print("something went wrong!")
            client.close()
            break

def write():
    while True:
        message = f": {input('')}"
        client.send(message.encode('ascii'))

revice_thread = threading.Thread(target=receive)
revice_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()