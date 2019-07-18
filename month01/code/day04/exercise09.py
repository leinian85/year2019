str1 = input("请输入一个字符串：")
for str in str1:
    print(ord(str))


while True:
    in_str = input("请输入一个编码：")
    if in_str == "":
        break
    else:
        print(chr(int(in_str)))



