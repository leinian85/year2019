import sys
import os
import re

gitignore = ("__init__.py", "目录.html", "目录.txt", "目录.md", ".idea", ".git", "System Volume Information")
dict_file = ("py", "txt", "html", "png", "iso", "docx", "jpeg", "jpg", "gitignore", "sql", "md")


class AutoDirectoty:
    def __init__(self, type="HTML"):
        """
        :param type: 要生成的文件格式  html/txt
        """
        self.directoty_txt = ""
        self.type = type

    def href_rule(self, file):
        """
        # 创建超链接的文件的规则
        :param file:文件名称
        :return:True(有超链接)False(没有超链接)
        """
        result = False
        # 如果文件不存在.就返回真
        if file.find(".") < 0:
            return True
        if not os.path.isfile(file):
            return True
        if file.split(".")[-1] in dict_file:
            return True
        return result

    def show_rule(self, file):
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

    def get_path(self):
        # 按照/切割取到最后一个/的位置
        path = re.findall(r"(.*)/(.+)", __file__)
        return path[0][0] if path else "."

    def __txt_to_html(self):
        top = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>目录</title>
</head>
<body>

        """
        botton = """
</body>
</html>
"""
        self.directoty_txt = top + self.directoty_txt + botton

    def writefile(self):
        """
        将读出的文件和文件夹写入到文本文件
        :return:
        """
        file = "目录." + self.type
        with open(file, "w") as f:
            f.write(self.directoty_txt)

    def get_indent_flag(self, level):
        """
        获取缩进符号
        :param level:
        :return:
        """
        flag = "&nbsp;" if self.type.upper() == "HTML" else " "
        return flag * (level - 1) * 4 if level > 1 else ""

    def get_html_list(self, level, file_path):
        """
        将文件夹下的内容转换成html格式
        :param level:文件夹层级
        :param file_path:文件夹路径(绝对路径,如果是在U盘中,就是相对路径)
        :return:
        """
        dir = False
        flag = "&nbsp;" if self.type.upper() == "HTML" else " "
        indent_flag = flag * (level - 1) * 4 if level > 1 else ""

        for file in os.listdir(file_path):
            if file not in gitignore:
                url = file_path + "/" + file
                file_name = file if os.path.isfile(url) else "&blacktriangleright;[" + file + "]"
                if file.split(".")[-1] in dict_file or not os.path.isfile(url):
                    self.directoty_txt = (self.directoty_txt + indent_flag + '<a href ="%s">' + file_name +
                                          "</a><br/>" + "\n") \
                                         % url
                else:
                    self.directoty_txt = self.directoty_txt + indent_flag + file_name + "<br/>" + "\n"

                if not os.path.isfile(url):
                    dir = True
                    new_level = level + 1
                    new_path = file_path + "/" + file
                    self.get_html_list(new_level, new_path)
        if not dir:
            return


def main():
    level = 1
    ad = AutoDirectoty()
    path = ad.get_path()
    ad.get_html_list(level, path)
    ad.writefile()


"""
[目录1]
    文件1
    文件2
    文件3
    [目录1-1]
    文件1
    文件2
[目录2]
    文件1
    [目录2-2]
"""
if __name__ == '__main__':
    main()
    # ad = AutoDirectoty()
    # result = ad.rule("txt")
    # print(result)
