'''
判断一个年份是否是闰年
闰年：年份能被4整除，但是不能被100整除
     或者能被400整除
'''
year = int(input("请输入一个年份："))
result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(result)
