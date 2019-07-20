"""
客户端
建立网络连接
"""
import sys

sys.path.append("/home/tarena/1905/gittarena/month02/project_month02/")
import socket
from client.view import ShowView
from user.user_info import User
import sys
import time


class DictClient:
    def __init__(self):
        self.ADDR = ("127.0.0.1", 18629)

    def main(self):
        # 创建TCP套接字
        s = socket.socket()
        s.connect(self.ADDR)
        show = ShowView()
        try:
            while True:
                select = show.show_main()
                if select:
                    userinfo = select.split(" ")
                    user = User(userinfo[1], userinfo[2])
                    s.send(select.encode())
                    data = s.recv(1024).decode().split(" ")
                    if userinfo[0] == "2":
                        if data[0] == "Y":
                            user.user_id = data[1]
                            show.show_tow(user,s)
                        else:
                            print("账号密码错误")
                    time.sleep(1)
                else:
                    return
        except KeyboardInterrupt:
            sys.exit("客户端退出")
