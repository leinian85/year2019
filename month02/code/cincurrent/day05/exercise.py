"""
select
"""
import socket
from select import select

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("127.0.0.1", 18629))
s.listen(3)
rlist = [s]
wlist = []
xlist = []

while True:
    rs, ws, xs = select(rlist, wlist, xlist)

    for i in rs:
        if i is s:
            c, addr = i.accept()
            print("connect from ", addr)
            rlist.append(c)
        else:
            data = i.recv(1024)
            if not data:
                rlist.remove(i)
                i.close()
                continue
            print(data.decode())
            wlist.append(i)

    for w in wlist:
        w.send(b"OK")
        wlist.remove(w)
