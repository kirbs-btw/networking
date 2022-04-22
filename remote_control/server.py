import threading
import socket
import datetime

clients = []
PORT = 55555
HOST = socket.gethostbyname(socket.gethostname())
print(HOST)

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((HOST, PORT))
SERVER.listen()
"""
def broadcast(message):
    print(message)
    for client in clients:
        client.send(message)
"""

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(message.decode('ascii'))
        except:
            clients.remove(client)
            client.close()
            break


def connect():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{now} Server status:        ONLINE")

    while True:
        client, address = SERVER.accept()
        print(f"Conneted with {str(address)}")

        clients.append(client)
        #client.send(encrypt('Connected to the server').encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

def sendReq():
    while True:
        req = input(": ")
        for client in clients:
            client.send(req.encode('ascii'))

if __name__ == '__main__':
    connect_thread = threading.Thread(target=connect)
    connect_thread.start()
    write_thread = threading.Thread(target=sendReq)
    write_thread.start()
