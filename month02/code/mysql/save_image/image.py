from mysql import MysqlExc

class SaveImage():
    def __init__(self):
        self.con_mysql = MysqlExc()

    def save(self,file):
        with open(file,"rb") as f:
            data = f.read()
        try:
            sql = "insert into image(image) values(%s)"
            self.con_mysql.cur.execute(sql,[data])
            self.con_mysql.db.commit()
        except Exception as e:
            self.con_mysql.db.rollback()
            print(e)

    def get(self,file):
        sql = "select image from image"
        self.con_mysql.cur.execute(sql)
        for image in self.con_mysql.cur.fetchall():
            with open(file,"wb+") as f:
                f.write(image[0])

