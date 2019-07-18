"""
httpserver V1.0
基本要求:1.获取来自浏览器的请求
        2.判断如果请求的内容是/ 将 index.html返回给客户

"""
import socket

def request(confd):
    data = confd.recv(4096)
    print(data.decode().split(" ")[1])

    if not data:
        return

    response = ""
    if data.decode().split(" ")[1] == "/":
        with open("index.html") as f:
            response  =  """http/1.1 200 OK
Content-Type:Text/html

            """
            response += f.read()
    else:
        response = """http/1.1 404 NOT FOUND
Content-Type:Text/html

<h1>SORRY...</h1>
                    """
    return response

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind(("127.0.0.1",18629))
s.listen(3)

while True:
    c,addre = s.accept()
    response = request(c)
    c.send(response.encode())