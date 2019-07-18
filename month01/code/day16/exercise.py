# 练习：员工管理器记录多个员工
#      迭代员工管理器对象

class Employee:
    pass

class Employeeiter:
    def __init__(self,tager):
        self.__tager = tager
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__tager)-1:
            raise StopIteration
        em = self.__tager[self.__index]
        self.__index +=1
        return em


class EmployeeManager:
    def __init__(self):
        self.__employees = []

    def add_employee(self, emp):
        self.__employees.append(emp)

    def __iter__(self):
        return Employeeiter(self.__employees)

em = EmployeeManager()
em.add_employee("张三")
em.add_employee("李四")
em.add_employee("张无忌")

for item in em:
    print(item)
