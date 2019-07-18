'''
    元组
    元组的操作的
'''
month = int(input("请输入月份"))
if month < 1 or month > 12:
    print("输入有误")
elif month in (4, 6, 9, 11):
    print("31天")
elif month == 2:
    print("28天")
else:
    print("30天")
