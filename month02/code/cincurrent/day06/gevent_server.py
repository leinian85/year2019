"""
gevent server
"""
import gevent
from gevent import monkey
monkey.patch_socket() #执行脚本,修改socket阻塞
from socket import *
def handle(client):
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(data.decode())
        client.send(b"OK")


s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("127.0.0.1",18629))
s.listen(1)

while True:
    c,addr = s.accept()
    print("connect from",addr)
    # handle(c)
    gevent.spawn(handle,c)
