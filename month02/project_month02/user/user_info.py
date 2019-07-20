import sys
sys.path.append("/home/tarena/1905/gittarena/month02/project_month02/")
from database.con_mysql import ConMysql
class User:
    def __init__(self,name,password,user_id = None):
        self.user_id = user_id
        self.name = name
        self.password = password