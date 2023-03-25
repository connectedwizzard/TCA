import socket
import threading

# Change this to the IP address you want the server to listen on
HOST = '127.0.0.1'
PORT = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []

def handle_client(client_socket, address):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode()
        print(f'{address[0]}:{address[1]} - {message}')
        broadcast(message, client_socket)

    client_socket.close()
    clients.remove(client_socket)

def broadcast(message, sender_socket):
    for client_socket in clients:
        if client_socket != sender_socket:
            client_socket.sendall(message.encode())

while True:
    client_socket, address = server_socket.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket, address))
    thread.start()

    message = f'New client connected: {address[0]}:{address[1]}'
    print(message)
    broadcast(message, client_socket)
