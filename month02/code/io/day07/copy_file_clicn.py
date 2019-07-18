from socket import socket

clickfd = socket()
clickfd.connect(("176.215.133.140",18629))
with open("111.txt","rb") as f:
    name = "name=111.txt"
    clickfd.send(name.encode())
    clickfd.send(f.read())
    data = clickfd.recv(1024)
    print(data.decode())