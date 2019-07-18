students = {}
while True:
    name = input("姓名：")
    if name == "":
        break
    age = int(input("年龄："))
    score = float(input("成绩："))
    sex = input("性别：")
    student = {}
    student["年龄"] = age
    student["成绩"] = score
    student["性别"] = sex
    students[name] = student

for k,v in students.items():
    print("%s 性别：%s 年龄：%d 成绩：%.2f"%(k,v["性别"],v["年龄"],v["成绩"]))


