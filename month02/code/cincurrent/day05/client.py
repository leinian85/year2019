import socket
c = socket.socket()
c.connect(("127.0.0.1",18629))
while True:
    data = input(">>")
    c.send(data.encode())
    data_from = c.recv(1024)
    print(data_from.decode())