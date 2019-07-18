import socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) # 端口马上可以使用
s.bind(("176.215.133.140",18629))
s.listen()
c,addr = s.accept()
print(s.family)# 地址类型 AddressFamily.AF_INET
print(s.type) #套接字类型 SocketKind.SOCK_STREAM
print(s.getsockname())  #服务端地址 ('176.215.133.140', 18629)
print(s.fileno()) # 文件描述符/文件号
print(c.getpeername()) # 客户端地址 ('176.215.133.140', 56476)