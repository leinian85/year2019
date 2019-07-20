"""
dict 服务端
功能 : 业务逻辑处理
模型 : 多进程 tcp 并发
封装 : 方法
"""
import sys

sys.path.append("/home/tarena/1905/gittarena/month02/project_month02/")
import socket
from multiprocessing import Process
import signal
from bll.register import Register
from user.user_info import User
from database.con_mysql import ConMysql
from bll.dict import UserDict


class DictServer:
    def __init__(self):
        HOST = "127.0.0.1"
        PORT = 18629
        self.ADDR = (HOST, PORT)

    def request(self, client, con):
        # 循环接受请求
        while True:
            data = client.recv(4096).decode()
            if not data:
                sys.exit()  # 对应子进程退出
            data = data.split(" ")
            flag = data[0]
            print(data)
            if flag in ("1", "2"):
                user = User(data[1], data[2])
                bll = Register(con, user)
                if flag == "1":  # 注册
                    client.send(bll.register().encode())
                else:  # 登录
                    client.send(bll.login().encode())
            else:
                user_id = data[1]
                bll = UserDict(con)
                send_str = ""
                print("user_id", user_id)
                if flag == "21":  # 翻译
                    word = data[2]
                    bll.save_log(user_id, word)
                    result = bll.select_word(word)
                    if result:
                        for item in result:
                            send_str = item[0] + "###"
                    else:
                        send_str = "没有找到该单词"

                elif flag == "22":  # 查看明细
                    result = bll.select_history(user_id)
                    print("result", result)
                    for item in result:
                        send_str += item[0] + " " + item[1] + " " + str(item[2])+"###"

                print("将要发送的内容", send_str)
                send_str = send_str.encode()
                client.send(send_str)

    def main(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(self.ADDR)
        s.listen(5)

        # 处理僵尸进程
        signal.signal(signal.SIGCHLD, signal.SIG_IGN)

        print("waitting client connect...")
        con = ConMysql()
        while True:
            try:
                c, addr = s.accept()
                print("connect from ", addr)
            except KeyboardInterrupt:
                s.close()
                sys.exit("服务器退出")
            except Exception as e:
                print("Error:", e)
                continue

            p = Process(target=self.request, args=(c, con))
            p.daemon = True  # 父进程退出时子进程也退出
            p.start()  # 启动子进程
