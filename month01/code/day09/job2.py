class People:
    def __init__(self,type):
        self.type = type

    def print_info_list(self):
        print("我是%s"%self.type)

people = People("外星人")
people.print_info_list()
