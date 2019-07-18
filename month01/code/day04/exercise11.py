# ﻿day04　作业
# 1. 三合一
# 2. 独立完成当天练习
# 3.  按照以下格式，输出变量name = "悟空",age = 800,score = 99.5
#      我叫xx,年龄是xx,成绩是xx。
name = "悟空"
age = 800
score = 99.5
print("我叫%s,年龄是%d,成绩是%.1f。" %(name,age,score))

# 4.　在控制台中获取一个整数作为边长．
# 　　根据边长打印矩形．
#    例如：４
#        ****
#        *  *
#        *  *
#        ****
#
#        6
#        ******
#        *    *
#        *    *
#        *    *
#        *    *
#        ******
num1 = int(input("请输入一个数："))
for item in range(1,num1+1):
    if item in (1,num1):
        print("*"*num1)
    else:
        print("*"+" "*(num1-2)+"*")

# 5.在控制台中录入一个字符串，判断是否为回文．
#   判断规则:正向与反向相同．
#   　　　上海自来水来自海上
message = input("请输入一个字符串：")
message2 = message[::-1]
if message == message2:
    print("是回文")
else:
    print("不是回文")


# 6. (扩展)一个小球从１００ｍ的高度落下
#     　　每次弹回原高度的一半．
#     　　计算：总共弹起来多少次（最小弹起高度0.01ｍ）．
#             总共走了多少米
weight = 100
sum = weight
count = 0
while True:
    weight /= 2
    if weight<=0.01:
        break
    sum += (weight * 2)
    count += 1
print("总共弹起来%d次,总共走了%.2f米" %(count,sum))

# 7. 看教程 www.runoob.com
#    看文档 docs.python.org/zh-cn/3/
#    逛社区 www.pythontab.com
