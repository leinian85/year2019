from con_mysql import ConMysql
import re

class DictCortrol():
    def __init__(self):
        self.con_mysql = ConMysql()

    def add(self,word,exp):
        sql = "insert into words(word,exp) values(%s,%s)"
        self.con_mysql.cur.execute(sql,[word,exp])

    def add_all(self):
        with open("dict.txt","r") as f:
            try:
                for line in f.readlines():
                    tup = re.findall(r"(\S+)\s+(.*)",line)[0]
                    self.add(tup)
                self.con_mysql.db.commit()
            except Exception as e:
                self.con_mysql.db.rollback()
                print(e)




