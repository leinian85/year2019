"""
文件读写
"""
file_= open("1.txt","r")
# while True:
#     data = file_.read(2)
#     # if data is None:  # None 和 "" 的区别
#     if data == "":
#         break
#     print(data)

file02 = file_.readlines()
for line in file02:
    print(line.replace("\n",""),end=" ")

a = ""
b = ''
print(a is b)
