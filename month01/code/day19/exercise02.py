import time

def validate(func):
    def wrapper(*args, **kwargs):
        time01 = time.time()
        func(*args, **kwargs)
        time02 = time.time()
        print("%s执行了%d秒"%(func.__name__,time02-time01))
    return wrapper

@validate
def fun01():
    time.sleep(2)
    print("fun01执行完毕")

@validate
def fun02():
    time.sleep(5)
    print("fun02执行完毕")

fun01()
fun02()
