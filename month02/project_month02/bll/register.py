import sys

sys.path.append("/home/tarena/1905/gittarena/month02/project_month02/")

"""
import hashlib

#生产加密对象
hash = hashlib.md5()

#对密码进行加密,passwd为明文密码
hash.update(passwd.encode())


pwd = hash.hexdigest()
"""


class Register:
    def __init__(self, con, user):
        self.con = con
        self.user = user

    def __is_exist(self):
        sql = "select count(1) from users where name = %s"
        try:
            self.con.cur.execute(sql, [self.user.name])
            data = self.con.cur.fetchone()[0]
            if data > 0:
                return True
            else:
                return False
        except Exception:
            return True

    def __save_user(self):
        sql = "insert into users(name,password) values(%s,%s)"
        try:
            self.con.cur.execute(sql, [self.user.name, self.user.password])
            self.con.db.commit()
            return "Y 注册成功"
        except Exception as e:
            self.con.db.rollback()
            return "N " + e

    def register(self):
        if self.__is_exist():
            return "N 用户已经存在"
        else:
            return self.__save_user()

    def login(self):
        sql = "select user_id from users where name = %s and password = %s"
        try:
            self.con.cur.execute(sql, [self.user.name, self.user.password])
            data = self.con.cur.fetchone()
            if data:
                return "Y " + str(data[0])
            else:
                return "N"
        except Exception:
            return "N"
