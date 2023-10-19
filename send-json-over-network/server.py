import json
import socket

ip = socket.gethostbyname(socket.gethostname())
port = 5000

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_port = (ip, port)

sock_server.bind(ip_port)

sock_server.listen(5)

credential = {
        "username": "david",
        "password": "davidjoy"
    }

while True:
    print(
        "Server up waiting for connection \n"
        "CTRL-C to close server"
          )
    client, addr = sock_server.accept()
    print(client)
    print(f"{addr} connected")
    
    data = json.loads(
        client.recv(1024).decode()
    )

    checks = (
        data["username"] == credential["username"],
        data["password"] == credential["password"]
    )

    if all(checks):
        client.send("Successfully connected".encode())
        print("Successfully connected")

    else:
        client.send("Failed to connect".encode())
        print("Failed to connect")

    
