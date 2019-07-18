import os
import time

def f01():
    for i in range(4):
        time.sleep(3)
        print("写代码")

def f02():
    for i in range(4):
        time.sleep(1)
        print("测试代码")

pid = os.fork()

if pid < 0:
    print("ERROR")
elif pid == 0 :
    p = os.fork()
    if p == 0:
        f01()
    else:
        os._exit(0)
else:
    os.wait()
    f02()