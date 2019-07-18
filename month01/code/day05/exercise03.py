list_name = []
while True:
    name = input("姓名：")
    if name == "":
        break
    if name in list_name:
        print("姓名已经存在，不能添加到列表中")
    else:
        list_name.append(name)

for item in range(len(list_name)-1,-1,-1):
    print(list_name[item])
