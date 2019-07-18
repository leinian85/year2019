"""
thread2 线程参数演示
"""
from threading import Thread
from time import sleep

def fun(sec,name):
    print("===========")
    sleep(sec)
    print("====%s====="%name)

# 创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=fun,args=(1,),kwargs={"name":"NAME%d"%i})
    t.start()
    jobs.append(t)

for i in jobs:
    i.join()


