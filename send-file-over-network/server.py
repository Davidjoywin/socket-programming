import socket

ip = ''
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(1)
while True:
    client, addr = server.accept()
    print(client)
    print(addr)
    with open('test_img.jpg', 'rb') as test:
        client.sendfile(test)
