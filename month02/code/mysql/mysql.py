import pymysql
import stu_class
import mysql_parameter


class MysqlExc:
    def __init__(self):
        # 连接数据库
        myparament = mysql_parameter.MysqlParameter()
        self.db = pymysql.connect(host=myparament.host,
                                  port=myparament.port,
                                  user=myparament.user,
                                  password=myparament.password,
                                  database=myparament.database,
                                  charset=myparament.charset)
        # 获取游标
        self.cur = self.db.cursor()

    def add(self, stu):
        sql = "insert into class(name,age,sex,score,入学时间) " \
              "values(%s,%s,%s,%s,curdate())"
        try:
            self.cur.execute(sql, [stu.name, stu.age, stu.sex, stu.score])
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)

    def update(self, stu):
        sql = "update class set name = '%s',age = %d,sex = '%s',score = %f,入学时间 = '%s' where id = %d" \
              % (stu.name, stu.age, stu.sex, stu.score, stu.入学时间, stu.id)
        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)

    def delte(self, id):
        sql = "delete from class where id = %d" % id
        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)

    def select(self):
        sql = "select * from class;"
        self.cur.execute(sql)
        row = self.cur.fetchall()
        for item in row:
            print(item)


# MysqlExc = MysqlExc()
# stu = stu_class.StuClass("鸠摩智", 49, "男", 70)
# MysqlExc.add(stu)
# # stu = stu_class.StuClass("张三丰", 108, "男", 98, date = "2019-5-18",id = 4)
# # MysqlExc.update(stu)
# # MysqlExc.delte()
# MysqlExc.select()
