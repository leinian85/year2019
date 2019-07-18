import random

scors = 0
print("考试开始...")
for i in range(3):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    sum = int(input(str(num1) + " + " + str(num2) + " = "))
    if num1 + num2 == sum:
        scors += 10
        print("得10分")
    else:
        print("不得分")
print("总分：" + str(scors))
