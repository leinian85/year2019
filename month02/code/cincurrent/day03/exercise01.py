from multiprocessing import Process,Pipe

# 创建管道
fd1,fd2 = Pipe()

def app1():
    print("启动app1 请登录")
    print("请求app2 授权")
    fd1.send("app1请求登录")
    data = fd1.recv()
    if data:
        print("登陆成功:",data)


def app2():
    data = fd2.recv()
    print(data)
    fd2.send(("Dave","123"))

p1 = Process(target=app1)
p2 = Process(target=app2)
p1.start()
p2.start()
p1.join()
p2.join()