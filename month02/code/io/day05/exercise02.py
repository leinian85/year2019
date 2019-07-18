"""
file操作
"""
file_object = open("1.txt",mode="w")
print(file_object)  #<_io.TextIOWrapper name='1.txt' mode='w' encoding='UTF-8'>
file2 = open("1.txt","r+")
print(file2)
file3 = open("5.txt","a")
print(file3)

