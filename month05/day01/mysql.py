import pymysql

db = pymysql.connect(host="127.0.0.1", user="root", password="123456",
                 database="blog", port=3306,charset='utf8')
cursor = db.cursor()

sql = "update user_profile set info = '123456'"

res = cursor.execute(sql)
print(res)