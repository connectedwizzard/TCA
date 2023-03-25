# TCA - Terminal Chat Application
The Python script for the chat app is a simple client-server model that allows two users to exchange messages with each other. The server script listens for incoming connections on a specified IP address and port number, while the client script connects to the server using the same IP address and port number.
### Extra: IP Change
To change the IP address in `server.py` and `client.py`, you can modify the `HOST` variable at the top of each script. Simply replace `127.0.0.1` with the IP address you want to use.
## server.py
The `server.py` script creates a socket and listens for incoming connections on the specified host and port.
## client.py
The `client.py` script creates a socket and connects to the server on the specified host and port.
