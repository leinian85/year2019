# 作业:调用fun07。
def fun07(a, b, *args, c, d, **kwargs):
    pass

fun07(1,2,c=2,d=4)
fun07(1,2,1,2,3,c=3,d=1,e=1,f=2)


# day08
# 1. 三合一
# 2. 当天练习独立完成
# 3. 自学(参照菜鸟教程)字符串/列表/字典常用函数(方法),实现如下功能。
#     字符串："　校　训：自　强不息、厚德载物。　　"
str01 = "　校　训：自　强不息、厚德载物。　　"
#     查找空格的数量
print(str01.count("　"))
#     删除字符串前后空格
print(str01.strip())
#     删除字符串所有空格
print(str01.replace("　",""))
#     查找"载物"的位置
print(str01.find("载物"))
#     判断字符串是否以"校训"开头.
print(str01.startswith("校训"))
str02 = str01.replace("　","")
print(str02.startswith("校训"))

# 4. 定义函数，计算指定范围内的素数
def get_prime_number(start,end):
    list_number = []
    for item in range(start,end+1):
        flag = False
        if item > 2:
            if if_prime(item):
                list_number.append(item)
    return list_number


def if_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


print(get_prime_number(15,90))
# 5. 群讨论：is  与 == 的区别
a = [1,2]
b = [1,2]
print(a is b)   # is 判断的是引用是否相同
print(a == b)   # == 判断的是内容是否相同
# 6. 玩2048游戏(了解游戏规则).
# 7. 重构 shopping.py 程序
#    不改变原有功能，修改程序代码。
# 8. 阅读:python入门到实践第8章