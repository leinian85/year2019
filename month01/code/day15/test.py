import time
#返回时间戳,从1970-01-01开始算起到现在经过的秒数
a = time.time()
print(a)  # 1561027851.4983401

#返回本地时间
#格式：时间元组格式,可以用索引取值
# time.struct_time(tm_year=2019, tm_mon=6, tm_mday=20, tm_hour=18,
# tm_min=50, tm_sec=51, tm_wday=3, tm_yday=171, tm_isdst=0)
time.localtime()

#返回"%Y-%m-%d %H:%M:%S"格式的字符串
a = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(a)  # 2019-06-20 18:54:03

#让系统沉睡几秒
time.sleep(5) #系统停顿5秒再执行接下来的程序

try:
    age = int(input("请输入年龄:"))
except ValueError:
    print("输入错误")
except Exception:
    print("输入错误")