"""
httpserver v2.0
env: python3.6
io多路复用 和 http训练
"""

from socket import *
from select import *

# 具体功能实现
class HTTPServer:
    def __init__(self,host='0.0.0.0',port=8000,dir=None):
        self.host = host
        self.port = port
        self.dir = dir
        self.address = (host,port)


# 用户使用HTTPServer
if __name__ == "__main__":
    """
    通过 HTTPServer类快速搭建服务，展示自己的网页
    """
    # 用户决定的参数
    HOST = '0.0.0.0'
    PORT = 8000
    DIR = './static' # 网页存储位置

    httpd = HTTPServer(HOST,PORT,DIR) # 实例化对象
    httpd.serve_forever() # 启动服务









