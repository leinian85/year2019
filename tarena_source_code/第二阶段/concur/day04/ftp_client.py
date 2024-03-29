"""
ftp 文件服务，客户端
"""
from socket import *
import sys

# 服务器地址
ADDR = ('127.0.0.1', 8080)


# 客户端文件处理类
class FTPClient:
    """
    客户端处理 查看，上传，下载，退出
    """

    def __init__(self, sockfd):
        self.sockfd = sockfd

    # 获取文件库中文件列表
    def do_list(self):
        self.sockfd.send(b'L')  # 发送请求
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            # 一次接收文件字符串
            data = self.sockfd.recv(4096)
            print(data.decode())
        else:
            print(data)

    # 退出
    def do_quit(self):
        self.sockfd.send(b'Q') # 请求退出
        self.sockfd.close()
        sys.exit('谢谢使用')

    # 下载文件
    def do_get(self,filename):
        # 发送请求
        self.sockfd.send(('G '+filename).encode())
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            f = open(filename,'wb')
            # 循环接收写入文件
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##': # 发送完成
                    break
                f.write(data)
            f.close()
        else:
            print(data)

# 链接服务器
def main():
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return

    # 实例化对象，调用文件处理方法
    ftp = FTPClient(sockfd)

    # 循环发送请求
    while True:
        print("\n=========命令选项=========")
        print("*****      list      *****")
        print("*****    get file    *****")
        print("*****    put file    *****")
        print("*****      quit      *****")
        print("===========================")

        cmd = input("输入命令: ")
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd[:3] == 'get':
            filename=cmd.strip().split(' ')[-1]
            ftp.do_get(filename)
        else:
            print("请输入正确命令")


if __name__ == "__main__":
    main()
