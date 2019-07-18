from con_mysql import ConMysql
from user_model import UserModel
class Register:
    def __init__(self):
        self.con = ConMysql()

    def is_exit(self,name,password):
        user = UserModel(name, password)
        sql = "select password from users where name = %s"
        self.con.cur.execute(sql, [name])
        data = self.con.cur.fetchone()
        if not data:
            return (False,None)
        else:
            return (True,data[0])

    def register(self,name,password):
        info = self.is_exit(name, password)
        if not info[0]:
            sql = "insert into users(name,password) values(%s,%s)"
            try:
                self.con.cur.execute(sql,[name,password])
                self.con.db.commit()
                return True
            except Exception as e:
                self.con.db.rollback()
                return False

    def login(self,name,password):
        info = self.is_exit(name,password)
        if info[0] and password == info[1]:
            return True
        return False
