"""
chat room  客户端
发送请求，展示结果
"""
from socket import *
import os,sys

# 服务器地址
ADDR = ('127.0.0.1',8888)

#客户端启动函数
def main():
    s = socket(AF_INET,SOCK_DGRAM)

    # 进入聊天室
    while True:
        name = input("请输入姓名:")
        msg = 'L ' + name
        s.sendto(msg.encode(),ADDR)
        #　接收反馈
        data,addr = s.recvfrom(128)
        if  data.decode() == 'OK':
            print("您已进入聊天室")
            break
        else:
            print(data.decode())

main()

