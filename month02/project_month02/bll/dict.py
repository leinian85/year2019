import sys
sys.path.append("/home/tarena/1905/gittarena/month02/project_month02/")
class UserDict:
    def __init__(self,con):
        self.con = con

    def select_word(self,word):
        sql = "select exp from words where word = %s"
        try:
            self.con.cur.execute(sql, [word])
            data = self.con.cur.fetchall()
            return data
        except Exception:
            return None

    def select_history(self, user_id):
        sql = "select a.name,b.word,b.time from users a,list_history b where a.user_id = b.user_id and " \
              "a.user_id = %s limit 10"
        try:
            self.con.cur.execute(sql, [user_id])
            data = self.con.cur.fetchall()
            return data
        except Exception:
            return None

    def save_log(self,user_id,word):
        sql = "insert into list_history(user_id,word) values(%s,%s)"
        try:
            self.con.cur.execute(sql,[user_id,word])
            self.con.db.commit()
        except Exception as e:
            self.con.db.rollback()
            print(e)

