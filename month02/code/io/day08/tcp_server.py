import socket

s = socket.socket()
s.bind(("127.0.0.1",18629))
s.listen(3)
c,addre = s.accept()
c.recv(1024)
response = """http/1.1 200 OK
Content-Type:Text/html

<h2>hello</h2>
"""
c.send(response.encode())
