"""
     3. 编写一个程序，向一个文件中写入如下内容：　
     　　1.  2019-1-1  18:18:18
     　　2.  2019-1-1  18:18:19
     　　3.  2019-1-1  18:18:24
        循环每隔１秒写入一次,序号从１排列
        ctrl-c结束程序，下次启动程序
        序号要与之前的衔接
"""
import sys
sys.path.append("/home/tarena/1905/month02/code")
from mytime.mytime import MyTime
import time


class Write:
    @staticmethod
    def write():
        # print(sys.path)
        file = open("temp.txt", "r+", buffering=1)
        num = 1
        mytime = MyTime()
        for item in file:
            # num = int(item.split(" ")[0]) + 1
            num += 1
        while True:
            file.write(str(num) + " " + mytime.my_date() + "\n")
            num += 1
            time.sleep(1)
        file.close()


w =Write()
w.write()
