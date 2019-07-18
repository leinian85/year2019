from config import Config
import pymysql


class ConMysql:
    def __init__(self):
        self.con = Config()
        self.db = pymysql.connect(host=self.con.host,
                                  port=self.con.port,
                                  user=self.con.user,
                                  password=self.con.password,
                                  database=self.con.database,
                                  charset=self.con.charset)
        self.cur = self.db.cursor()
