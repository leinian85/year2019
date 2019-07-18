num = int(input("请输入一个整数："))
state = "奇数" if num % 2 else "偶数"
print(state)

year = int(input("请输入一个年份"))
result = ("闰年" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0
          else "不是闰年")
print(result)
