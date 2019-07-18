class Student:
    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_info(self):
        print("姓名：%s 年龄：%d 分数：%d 性别：%s" % (self.name, self.age, self.score, self.sex))