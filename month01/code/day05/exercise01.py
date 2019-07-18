list01 = []
while True:
    name = input("输入你喜欢的人物：")
    if name == " ":
        break
    list01.append(name)

for index in range(0,len(list01)):
    print(list01[index])