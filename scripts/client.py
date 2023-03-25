import socket
import threading

# Change this to the IP address of the server you want to connect to
HOST = '127.0.0.1'
PORT = 8888

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_messages():
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode()
        print(message)

thread = threading.Thread(target=receive_messages)
thread.start()

while True:
    message = input('Enter message: ')
    client_socket.sendall(message.encode())
