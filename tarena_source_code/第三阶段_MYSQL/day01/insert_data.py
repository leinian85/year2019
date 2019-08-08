import pymysql
#建立连接
con = pymysql.connect('localhost',  'root', '123456','country', port=3306, charset='utf8')
#获取游标
cur = con.cursor()
#插入数据
data_list = []
for x in range(2000000):
    name = 'Tom_%s'%(x)
    data_list.append(name)


ins = 'insert into students(name) values(%s)'
cur.executemany(ins, data_list)
con.commit()

#关闭
cur.close()
con.close()











