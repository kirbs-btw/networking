import socket
import threading
import datetime

clients = []
host = socket.gethostbyname(socket.gethostname())
print(host)
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()



def broadcast(message):
    print(message)
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            clients.remove(client)
            client.close()
            break

def connect():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{now} Server status:        ONLINE")

    while True:
        client, address = server.accept()
        print(f"Conneted with {str(address)}")

        clients.append(client)
        client.send('Connected to the server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

if __name__ == '__main__':
    connect()