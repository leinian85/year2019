### time模块
>import time

- 1.返回时间戳,从1970-01-01开始算起到现在经过的秒数
    >a = time.time()
    print(a)  # 1561027851.4983401

- 2.返回本地时间 (年，月，日，时，分，秒，一周的第几天，一年的第几天，夏令时)
    >#格式：时间元组格式,可以用索引取值
    #time.struct_time(tm_year=2019, tm_mon=6, tm_mday=20, tm_hour=18,
    #tm_min=50, tm_sec=51, tm_wday=3, tm_yday=171, tm_isdst=0)
    time.localtime()
    print(tuple_time[1])  # 获取月

- 3.返回"%Y-%m-%d %H:%M:%S"格式的字符串
    >#时间元组 -->  str
    a = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    print(a)  # 2019-06-20 18:54:03

- 4.str  -->  时间元组
    >print(time.strptime(str_time01, "%Y / %m / %d %H:%M:%S"))

- 5.让系统沉睡几秒
    >time.sleep(5) #系统停顿5秒再执行接下来的程序
