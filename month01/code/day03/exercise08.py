'''﻿day03 作业
1. 三合一
2. 当天练习独立完成
3.在控制台中获取月份,显示季度,或者提示月份错误.'''
month = input("请输入月份：")
if month in ("1","2","3"):
    print("第一季度")
elif month in ("4","5","6"):
    print("第二季度")
elif month in ("7","8","9"):
    print("第三季度")
elif month in ("10","11","12"):
    print("第四季度")
else:
    print("输入有误")

'''4.在控制台中获取年龄，
如果小于０岁，打印输入有误
如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿。
如果一个人的年龄为2（含）～13岁，就打印一条消息，指出他是儿童。
如果一个人的年龄为13（含）～20岁，就打印一条消息，指出他是青少年。
如果一个人的年龄为20（含）～65岁，就打印一条消息，指出他是成年人。
如果一个人的年龄超过65（含）岁～150岁，就打印一条消息，指出他是老年人。
150岁以上，打印"那不可能"'''
age = int(input("请输入年龄："))
if age < 0:
    print("输入有误")
elif age < 2:
    print("他是婴儿")
elif age < 13:
    print("他是儿童")
elif age < 20:
    print("他是青少年")
elif age < 65:
    print("他是成年人")
elif age < 150:
    print("他是老年人")
else:
    print("那不可能")

'''
5.根据身高体重,参照BMI,返回身体状况.
 BMI:用体重千克数除以身高米数的平方得出的数字
 中国参考标准
 体重过低BMI<18.5
 正常范围18.5≤BMI<24
 超重24≤BMI<28
 I度肥胖28≤BMI<30
 II度肥胖30≤BMI<40
 Ⅲ度肥胖BMI≥40.0'''

weight = float(input("请输入体重(KG)："))
stature = float(input("请输入身高(M)："))
bmi = weight / stature**2
if bmi <18.5:
    print("体重过轻")
elif bmi <24:
    print("体重正常")
elif bmi <28:
    print("体重超重")
elif bmi <30:
    print("I度肥胖")
elif bmi <40:
    print("II度肥胖")
else:
    print("III度肥胖")

# 6.阅读：Python入门到实践 第5章。