"""
    定义员工管理器
        1.管理所有员工
        2. 计算所有员工工资

    员工：
        程序员：底薪 + 项目分红
        销售：底薪 + 销售额 * 0.05
        软件测试...
        ...

    要求：增加新岗位，员工管理器不变.
"""


class EmployeeManager:
    def __init__(self):
        self.__employee = []

    def set_employee(self, value):
        self.__employee.append(value)

    def calculate_pay(self):
        for item in self.__employee:
            print("%s的工资是%d" % (item.name, item.calculate_pay()))


class Employee:
    def calculate_pay(self):
        pass


class Programmer(Employee):
    def __init__(self, name, furthest_pay, melon_cutting):
        self.name = name
        self.furthest_pay = furthest_pay
        self.melon_cutting = melon_cutting

    def calculate_pay(self):
        return self.furthest_pay + self.melon_cutting


class Seller(Employee):
    def __init__(self, name, furthest_pay, saleroom):
        self.name = name
        self.furthest_pay = furthest_pay
        self.saleroom = saleroom

    def calculate_pay(self):
        return self.furthest_pay + self.saleroom * 0.05

class SoftwareTest(Employee):
    def __init__(self, name, furthest_pay, melon_cutting):
        self.name = name
        self.furthest_pay = furthest_pay
        self.melon_cutting = melon_cutting

    def calculate_pay(self):
        return self.furthest_pay + self.melon_cutting

em = EmployeeManager()
p1 = Programmer("程序员",6000,4000)
em.set_employee(p1)
# em.calculate_pay()
s1 = Seller("销售员",2500,1000000)
em.set_employee(s1)
# em.calculate_pay()
s2 = SoftwareTest("软件测试",2000,4000)
em.set_employee(s2)
em.calculate_pay()
