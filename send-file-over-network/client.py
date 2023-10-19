import socket

ip = 'localhost'
port = 8080

nbyte = 1000 * 1000 * 1000 * 4
client = socket.socket()
client.connect((ip, port))
byte_data = client.recv(nbyte)
with open('test_2.jpg', 'wb') as test:
    test.write(byte_data)
