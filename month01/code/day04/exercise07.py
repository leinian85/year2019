temp_num = int(input("请输入一个正数："))

for item in range(2, temp_num):
    if temp_num % item == 0:
        print("不是素数")
        break
else:
    print("是素数")
