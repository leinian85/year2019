"""
thread1 线程基础使用
步骤: 基本同process
    1.封装线程函数
    2.创建线程对象
    3.启动线程
    4.回收线程
"""
import threading
from time import sleep
import os

a = 1
def music():
    for i in range(3):
        sleep(3)
        print(os.getppid(),"播放:12345")
    global a
    print(a)
    a = 10000

thread = threading.Thread(target=music)
thread.start()
for i in range(4):
    sleep(1)
    print(os.getppid(),"asdfg")
thread.join()
print("main a=",a)
