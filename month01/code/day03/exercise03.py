mark = float(input("请输入成绩："))
if 90 < mark <= 100:
    print("优秀")
elif 60 <= mark <= 90:
    print("良好")
elif 0 <= mark < 60:
    print("不及格")
else:
    print("输入有误")
