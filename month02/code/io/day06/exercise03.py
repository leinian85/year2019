import os

os.path.getsize("1.txt") # 获取文件大小,文件不存在会报错
os.path.isfile("1.txt") # 判断是否是文件
os.path.exists("1.txt") # 判断文件是否存在
os.listdir(".") # 将目录下面的文件和文件夹打包成 list
os.remove("12.txt") # 移除文件 文件不存在会报错
