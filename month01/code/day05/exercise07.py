list_tmp = []
while True:
    str_tem = input("请输入：")
    if str_tem == "":
        break
    else:
        list_tmp.append(str_tem)
print(" ".join(list_tmp))

result = ""
while True:
    str_tmp = input("请输入：")
    if str_tmp == "":
        break
    else:
        result += str_tmp
print(result)
