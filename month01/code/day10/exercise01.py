class Student:
    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_info(self):
        print("姓名：%s 年龄：%d 分数：%d 性别：%s" % (self.name, self.age, self.score, self.sex))


# list_student = []
# while True:
#     print("请录入学生信息：")
#     name = input("姓名：")
#     if name == "":
#         break
#     age = int(input("年龄："))
#     score = int(input("分数："))
#     sex = input("性别：")
#     student = Student(name,age,score,sex)
#     list_student.append(student)

# for student in list_student:
#     student.print_info()
#
# print("第一个学生是：")
# list_student[0].print_info()
list01 = [
    Student("赵敏", 28, 100, "女"),
    Student("明玉", 28, 90, "女"),
    Student("张无忌", 28, 80, "男"),
    Student("苏大强", 69, 70, "男"),
    Student("张三丰", 108, 99, "男"),
    Student("小昭", 28, 98, "女")
]


def get_info_for_name(name, list01):
    for item in list01:
        if item.name == name:
            return item

def get_info_for_sex(sex, list01):
    list_stu_info = []
    for item in list01:
        if item.sex == sex:
            list_stu_info.append(item)
    return list_stu_info

def get_info_for_age(age):
    count = 0
    for item in list01:
        if item.age >= age:
            count += 1
    return count

def clear_zreo(list01,score):
    for item in list01:
        item.score = score

def get_name(list01):
    list_name = []
    for item in list01:
        list_name.append(item.name)
    return list_name

def get_max_age(list01):
    age = 0
    name = ""
    for item in list01:
        if age < item.age:
            age = item.age
            name = item.name
    return get_info_for_name(name, list01)

print("找苏大强--------")
stu =  get_info_for_name("苏大强", list01)
print("%s的年龄是%d,分数是%d,性别是:%s" % (stu.name, stu.age, stu.score, stu.sex))

print("找女同学--------")
list_stu = get_info_for_sex("女",list01)
for stu in list_stu:
    print("%s的年龄是%d,分数是%d,性别是:%s" % (stu.name, stu.age, stu.score, stu.sex))

print("找年龄大于30的同学--------")
count = get_info_for_age(30)
print(count)

print("将所有同学的成绩清0--------")
clear_zreo(list01,0)
for item in list01:
    print("%s的年龄是%d,分数是%d,性别是:%s" % (item.name, item.age, item.score, item.sex))

print("获取所有同学的名字--------")
names = get_name(list01)
for name in names:
    print("%s"%name,end=" ")
print("")

print("找年龄最大的--------")
item = get_max_age(list01)
print("%s的年龄是%d,分数是%d,性别是:%s" % (item.name, item.age, item.score, item.sex))
