import sys
sys.path.append("/home/tarena/1905/gittarena/month02/project_month02/")
from database.config import Config
import pymysql


class ConMysql:
    def __init__(self):
        config = Config()
        self.db = pymysql.connect(host=config.host,
                                  user=config.user,
                                  password=config.password,
                                  database=config.database,
                                  port=config.port,
                                  charset=config.charset)
        self.cur = self.db.cursor()
