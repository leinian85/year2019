"""
file_write.py
文件写操作演示
"""

#　打开文件
# f = open('test','w')
# f = open('img.jpg','wb')
f = open('test','a')  #　追加

#　写操作
# f.write("hello 死鬼\n".encode())
# f.write("哎呀，干啥".encode())

# 将列表写入 人为添加换行
l = ['hello world\n','哈哈哈']
f.writelines(l)

f.close()