import re

str = "ded/dqdwq/dqwq/1.py"
print(re.findall("(.*)/(.+)",str))
str = "dwq"
a = re.findall("^__[a-zA-Z]*",str)
print(a)


def show_rule(file):
    """
    文件或文件夹是否显示的规则
    :param file:文件名称
    :return:True(显示)False(不显示)
    """
    result = True
    # 以 __ 开头 并且以 __ 结尾的文件和文件夹不显示
    sule = re.findall("^__[a-zA-Z]*__$", file)
    if sule:
        return False
    return result

print(show_rule("__asas__"))