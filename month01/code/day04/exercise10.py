message = input("请输入一个字符串：")
print("打印第一个字符：%s" %(message[0]))
print("打印最后一个字符：%s" % message[-1])
print("打印倒数第三个字符：%s" % message[-3])
print("打印前2个字符：%s" % message[0:2])
print("倒序打印字符：%s" % message[::-1])
lens = len(message)
if lens % 2 == 1:
    print("如果个数是奇数，打印中间字符：%s" % message[lens//2])
