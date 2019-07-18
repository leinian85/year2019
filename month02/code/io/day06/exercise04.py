"""
socket server
"""
import socket

# 创建一个socket对象
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定IP地址
sockfd.bind(("0",18629))
# 设置监听
sockfd.listen(1)

#截取客户端数据
print("waiting...")
clinkfd,adrss = sockfd.accept()
# 收发数据
clinkfd.recv(1024)
clinkfd.send(b"OK!")

clinkfd.close()
sockfd.close()