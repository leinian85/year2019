class Car:
    def __init__(self, color=None, brand=None):
        self.color = color
        self.brand = brand

    def set_color(self, color):
        self.color = color

    def set_brand(self, brand):
        self.brand = brand

    def print_info(self):
        print("车的颜色是:%s" % self.color)
        print("车的品牌是:%s" % self.brand)


car = Car()
car.set_color("red")
car.set_brand("奥迪")
car.print_info()
