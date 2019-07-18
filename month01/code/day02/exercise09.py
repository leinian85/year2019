# # day02 作业：
# # 1. 三合一(图示，代码，理论)
# # 2. 当天练习独立完成
# # 3. 画出下列代码内存图
# # a = 1000
# # b = a
# # a = 5000
# # print(b)# ?
# # 4. 已知：加速度，初速度，时间
# # 　　计算：距离
# # 　　加速度　＝　(距离 - 初速度　×　时间) * 2 / 时间平方
# speed_add = float(input("加速度："))
# speed_start = float(input("初速度："))
# time = float(input("时间："))
# length = speed_add * time ** 2 / 2 + speed_start * time
# print("距离为：" + str(length))
#
# # 5. 温度
# # 　　摄氏度 = (华氏度 - 32) / 1.8
# # 　　华氏度 = 摄氏度 * 1.8  + 32
# #    开氏度＝ 摄氏度　＋　273.15
# #    (1)在控制台中获取华氏度，计算摄氏度。
# #    (1)在控制台中获取，计算华氏度。
# #    (1)在控制台中获取摄氏度，计算开氏度。
# fahrenheit = float(input("请输入华氏温度："))
# celsiur_scale = (fahrenheit - 32) / 1.8
# print("摄氏温度为：" + str(celsiur_scale))
#
# celsiur_scale = float(input("请输入摄氏温度："))
# fahrenheit = celsiur_scale * 1.8 + 32
# print("华氏温度为：" + str(fahrenheit))
#
# celsiur_scale = float(input("请输入摄氏温度："))
# kelvin = celsiur_scale + 273.15
# print("开氏温度为：" + str(kelvin))
# 6.　看书:python入门到实践：阅读前两章.
#         程序员的数学，阅读第三章。
# 7.（扩展）在控制台中获取总秒数，计算几小时零几分钟零几秒。
print("秒数转换：")
total_second = int(input("请输入总秒数："))
hour = total_second // (60 * 60)
# minute = (total_second - hour * 60 ** 2) // 60
minute = total_second // 60 % 60
# second = total_second - hour * 60 ** 2 - min * 60
second = total_second % 60
print("一共是" + str(hour) + "小时" + str(minute) + "分" + str(second) + "秒")
