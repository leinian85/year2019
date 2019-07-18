from config import Config
import pymysql


class ConMysql:
    def __init__(self):
        self.db = pymysql.connect(host=Config.localhost,
                                  port=Config.port,
                                  user=Config.user,
                                  password=Config.password,
                                  database=Config.database,
                                  charset=Config.charset)

        self.cur = self.db.cursor()
