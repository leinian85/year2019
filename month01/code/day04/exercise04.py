count = 0
while count < 3:
    str_mark = input("请输入成绩：")
    if str_mark == "":
        break
    mark = float(str_mark)
    if 90 < mark <= 100:
        print("优秀")
    elif 60 <= mark <= 90:
        print("良好")
    elif 0 <= mark < 60:
        print("不及格")
    else:
        print("输入错误")
        count += 1
else:
    print("成绩错误过多")
