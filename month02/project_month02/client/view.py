import sys

sys.path.append("/home/tarena/1905/gittarena/month02/project_month02/")
import os
import time
from user.user_info import User
from bll.register import Register

from getpass import getpass


class ShowView:
    @staticmethod
    def __register():
        while True:
            name = input("用户名:")
            # password = getpass("密码:")
            # password1 = getpass("再次输入密码:")
            # if password != password1:
            #     print("两次密码不一致")
            #     continue
            password = input("密码:")
            if " " in name or " " in password:
                print("用户名和密码不能有空格")
                continue
            return name + " " + password

    @staticmethod
    def show_main():
        while True:
            os.system("clear")
            print("""
************************************

     1.注册 2.登录 3.退出

************************************
""")
            result = input("请选择:")
            if result == "3":
                return
            else:
                return result + " " + ShowView.__register()

    @staticmethod
    def show_tow(user,s):
        str_top = user.name.rjust(40, "=")
        str_center = "      1.单词翻译  2.查询历史 3.退出     "
        str_last = "=".rjust(40, "=")

        while True:
            os.system("clear")
            print(str_top + "\n\n" + str_center + "\n\n" + str_last)
            result = input("请选择:")
            send_str = ""
            word = ""
            if result == "1":
                word = input("word:")
                if word == "":
                    print("输入有误")
                    time.sleep(1)
                    continue
                send_str = "2" + result + " " + user.user_id + " " + word
            elif result == "2":
                send_str = "2" + result + " " + user.user_id
            elif result == "3":
                return
            s.send(send_str.encode())
            data = s.recv(4096).decode()
            if data:
                list_data = data.split("###")
                if result == "1":
                    for item in list_data:
                        if item:
                            print(word+"      "+item)

                else:
                    for line in list_data:
                        print(line)

            else:
                print("没有找到结果...")

            str = input("按任意键继续...")