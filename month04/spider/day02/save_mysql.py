from urllib import request
from fake_useragent import UserAgent
import  re
import time
import random
import csv
import pymysql

class spider_movie:
    movies = []
    def __init__(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="123456",
            database="spider",
            port=3306,
            charset='utf8'
        )
        self.cursor = self.db.cursor()
        pass

    def set_useragent(self):
        ua = UserAgent()
        self.headers  = {"User-Agent":ua.random}

    def get_url(self,page):
        if page == 1:
            return "https://maoyan.com/board/4"
        else:
            baseurl = "https://maoyan.com/board/4?offset={}"
            offset = (page-1)*10
            url = baseurl.format(offset)
            return url

    def get_html(self,url):
        self.set_useragent()
        res = request.Request(url = url,headers=self.headers)
        return request.urlopen(res).read().decode()

    def get_info(self,html):
        pattern = re.compile('<dd>.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>',re.S)
        movie_infos = pattern.findall(html)

        for info in movie_infos:
            movie = [info[0],info[1].strip()[3:],info[2][5:15]]
            spider_movie.movies.append(movie)

    def sava_csv(self,file):
        with open("猫眼电影.csv","w") as f:
            writer = csv.writer(f)
            writer.writerow(["名称", "主演", "上映时间"])
            for line in file:
                writer.writerow(line)

    def save_csv_rows(self,file):
        with open("猫眼电影.csv","w",) as f:
            writer = csv.writer(f)
            writer.writerows(file)

    def save_mysql(self,file):
        sql = "insert into filmtab(name,star,time) values(%s,%s,%s)"
        self.cursor.executemany(sql,file)
        self.db.commit()
        self.cursor.close()

    def write_html(self):
        for page in range(1,11):
            url = self.get_url(page)
            print(url)
            html = self.get_html(url)
            self.get_info(html)
            time.sleep(random.randint(1,3))
        self.save_mysql(self.movies)

sm = spider_movie()
sm.write_html()