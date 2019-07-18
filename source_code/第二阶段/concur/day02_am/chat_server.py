"""
chat room
env: python3.6
socket udp & fork
"""

from socket import *
import os,sys

"""
全局变量: 很多封装模块都要用或者有一定的固定含义
"""
# 服务器地址
ADDR = ('0.0.0.0',8888)

# 存储用户 {name:address}
user = {}

# 登录
def do_login(s,name,addr):
    if name in user:
        s.sendto('该用户存在'.encode(),addr)
        return
    s.sendto(b'OK',addr) # 可以进入聊天室

    # 通知其他人
    msg = "欢迎'%s'进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name] = addr # 插入字典


#　处理请求
def do_request(s):
    while True:
        data,addr = s.recvfrom(1024)
        tmp = data.decode().split(' ') #　拆分请求
        # 根据不同的请求类型具体执行不同的事情
        # L 进入　　C 聊天　　Q 退出
        if tmp[0] == 'L':
            do_login(s,tmp[1],addr)  # 执行具体工作


# 搭建网络
def main():
    # udp服务端
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    #　请求处理函数
    do_request(s)

main()

