import socket
import time
sudp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sudp.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1) # 设置套接字可以发送广播

adress = ("176.215.133.255",8888)
data = "今天回去记得洗澡"
while True:
    time.sleep(1)
    sudp.sendto(data.encode(),adress)
    # c,addr = sudp.recvfrom(1024)
    # print(c.decode())
