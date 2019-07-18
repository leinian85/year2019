students = []
while True:
    name = input("姓名：")
    if name == "":
        break
    age = int(input("年龄："))
    score = float(input("成绩："))
    sex = input("性别：")
    student = {}
    student["姓名"] = name
    student["年龄"] = age
    student["成绩"] = score
    student["性别"] = sex
    students.append(student)

for item in students:
    print("%s 性别：%s 年龄：%d 成绩：%.2f"%(item["姓名"],item["性别"],item["年龄"],item["成绩"]))



