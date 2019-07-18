"""
IO多路复用实现并发
建立 fileno ==> IO对象字典用于IO查找
"""
from socket import *
from select import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("127.0.0.1",18629))
s.listen(3)

fdmap = {s.fileno():s}

p = poll()

p.register(s,POLLIN|POLLERR)

while True:
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            fdmap[c.fileno()] = c
            p.register(c,POLLIN|POLLERR)
            print("connect from ",addr)
        else:
        # elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                fdmap[fd].close()
                del fdmap[fd]
                p.unregister(fd)
                continue
            print(data.decode())
            fdmap[fd].send(b"OK")
