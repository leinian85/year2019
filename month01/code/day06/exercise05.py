students = {}
while True:
    name = input("姓名：")
    if name == "":
        break
    age = int(input("年龄："))
    score = float(input("成绩："))
    sex = input("性别：")
    list_info = [age,score,sex]
    students[name] = list_info

for k,v in students.items():
    print("%s 性别：%s 年龄：%d 成绩：%.2f"%(k,v[2],v[0],v[1]))


