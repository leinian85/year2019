from socket import *
import json
from select import select
from setttings import *

ADDR = (frame_id,frame_port)
#处理某一方面的请求
class Application:
    def __init__(self):
        self.sockfd = socket(AF_INET,SOCK_STREAM)
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.sockfd.bind(ADDR)

    def start(self):
        self.sockfd.listen(3)
        print("app start from %d"%frame_port)
        while True:
            c, addr = self.sockfd.accept()
            data = c.recv(1024).decode()
            print(json.loads(data))
            d = {"status": "200", "data": "xxxxxxx"}
            c.send(json.dumps(d).encode())

app = Application()
app.start() #启动应用服务
