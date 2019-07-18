import random

count = 0
random_number = random.randint(1, 100)
while True:
    count += 1
    guess_number = int(input("请猜一个数："))
    if guess_number == random_number:
        print("猜对了,一共猜了" + str(count) + "次")
        break
    elif guess_number > random_number:
        print("大了")
    else:
        print("小了")
