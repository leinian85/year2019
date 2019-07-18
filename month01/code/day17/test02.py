class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say(self):
        pass

class student(person):
    def __init__(self, name, age, score):
        super().__init__(name,age)
        self.score = score

    def say(self):
        print("学生")

class teacher(person):
    def __init__(self, name, age, work):
        super.__init__(name,age)
        self.work = work

    def say(self):
        print("老师")

class speak_controll():

    def speak(self,person):
        person.say()

s1 = student("张三",10,100)
sp =speak_controll()
sp.speak(s1)




