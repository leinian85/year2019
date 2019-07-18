import socket
ADDR = ("127.0.0.1",18629)
sockclient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg = input(">>")
    if not msg:
        break
    sockclient.sendto(msg.encode(),ADDR)
    data,addr = sockclient.recvfrom(1024)
    print(data.decode())

sockclient.close()

