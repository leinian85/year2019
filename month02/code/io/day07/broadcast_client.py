import socket

sudp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sudp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # 设置套接字可以接收广播
adress = ("176.215.133.255", 10001)
sudp.bind(adress)

while True:
    c, addr = sudp.recvfrom(1024)
    print(c.decode())
