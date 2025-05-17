# Их по разным папкам
# Это сервер
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))

server.listen()

while True:
    user, adres = server.accept()

    user.send(input().encode('utf-8'))

    data = user.recv(1024)
    print(data.decode('utf-8'))



# Это клиент
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 12345))

while True:
    data = client.recv(1024)
    print(data.decode('utf-8'))

    client.send(input().encode('utf-8'))
