minutes = int(input("请输入分钟："))
hours = int(input("请输入小时："))
days = int(input("请输入天数："))
total = minutes * 60 + hours * 60 ** 2 + days * 24 * 60 ** 2
print("总秒数为："+str(total))
