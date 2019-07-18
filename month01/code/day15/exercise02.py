def get_score():
    while True:
        try:
            score = int(input("请输入成绩"))
            if 0 <= score <= 100:
                return score
            else:
                print("成绩必须在0到100之间")
        except ValueError:
            print("请输入整数")

score = get_score()
print(score)