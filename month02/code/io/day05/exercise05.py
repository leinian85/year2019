"""
文件写操作
"""
file = open("1.txt","r+")
for line in file:
    print(line)
    file.write("aaa")
# file.writelines(["123\n","asd"])

file.close()