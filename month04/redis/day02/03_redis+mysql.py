# redis+hash+mysql组合使用
import redis
import pymysql
import hashlib


class UserEdit:
    def __init__(self):
        self.r = redis.Redis(host="leinian", port=6379, db=0)
        self.db = pymysql.connect(
            host="leinian",
            user="root",
            password="123456",
            port=3306,
            charset="utf8",
            database="blog"
        )
        self.cursor = self.db.cursor()

    # 获取用户信息并缓存到redis中
    def get_userinfo(self, username):
        sql = "select username,password,email from user where username = %s"
        self.cursor.execute(sql, [username])
        userinfo = self.cursor.fetchone()

        if userinfo:
            userinfo_dict = {
                "username": userinfo[0],
                "password": userinfo[1],
                "email": userinfo[2]
            }

            self.update_redis(username, userinfo_dict)
            return userinfo_dict
        else:
            return None

    # 更新数据到 redis 中
    def update_redis(self, username, userinfo):
        self.r.hmset(username, userinfo)
        self.r.expire(username, 30)

    # 打印用户信息
    def print_userinfo(self, username):
        userinfo = self.r.hgetall(username)
        if userinfo:
            for key in userinfo:
                print(key.decode(), self.r.hget(username, key).decode())
        else:
            userinfo = self.get_userinfo(username)

            if userinfo:
                for k in userinfo:
                    print("%s:%s" % (k, userinfo[k]))
            else:
                print("用户不存在")

    # 更新用户信息
    def update_info(self, username, password, email):
        hs = hashlib.md5()
        hs.update(password.encode())
        pwd = hs.hexdigest()

        try:
            sql = "update user set password = %s,email=%s where username = %s"
            code = self.cursor.execute(sql, [pwd, email, username])
            if code > 0:
                self.db.commit()
                print("更新成功")
            else:
                print("没有数据改变")
        except:
            self.db.rollback()
            print("更改失败")
            return
        userinfo = {
            "username": username,
            "password": pwd,
            "email": email
        }
        self.update_redis(username, userinfo)
        print("缓存更新成功")


if __name__ == "__main__":
    UE = UserEdit()
    username = "leinian"
    UE.update_info(username, '111111', 'leinian_2005@qq.com')
    UE.print_userinfo(username)
