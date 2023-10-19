import json
import socket


ip = socket.gethostbyname(socket.gethostname())
port = 5000

def getUser():
    username = input("Username: ")
    password = input("Password: ")
    details = {"username": username, "password": password}
    data = json.dumps(details)
    return data


def registerUser():
    username = input("Username: ")
    password = input("Password: ")
    verify_password = input("Verify Password: ")
    if password == verify_password:
        details = {"username": username, "password": password, "verify_password": verify_password}
        data = json.dumps(details)
        return data
    raise Exception("Password does not match!!")


while True:
    username, password = getUser()

    details = {"username": username, "password": password}
    data = json.dumps(details)

    sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_port = (ip, port)

    sock_client.connect(ip_port)

    sock_client.send(data.encode())
    data = sock_client.recv(1024)
    print(data.decode())

