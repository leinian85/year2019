"""
作业: 1. 熟悉文件的基本操作函数
　　　2. 编写一个文件拷贝程序，从终端输入一个文件，
　　　　　将文件保存在当前目录下
        * 文件类型不确定（可是文本文件，可能是二进制文件）
"""
def newname(file, postfix):
    """
    根据传入的文件名,创建一个新的文件名
    :param file: 原始文件的文件名
    :param postfix: 新文件名的后缀
    :return: 返回新的文件的名称
    """
    file_name = file.split("/")[-1]
    name = file_name.split(".")
    name[0] += postfix
    return ".".join(name)


def file_copy(file):
    """
    复制文件到当前文件夹
    :param file: 要复制的文件
    """
    name_new = newname(file,"_copy")
    try:
        file = open(file,"rb")
        file_new = open(name_new,"wb")
        for item in file:
            file_new.write(item)
    except FileNotFoundError as e:
        print(e)
# "/home/tarena/1905/source_code/第一阶段/day01/day01/执行过程.jpg"
file = input("请输入一个文件:")
file_copy(file)