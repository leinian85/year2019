month = input("请输入月份：")
if month in ("1","3","5","7","8","10","12"):
    print("31天")
elif month in ("4","6","9","11"):
    print("30天")
elif month == "2":
    print("28天")
else:
    print("输入有误！")