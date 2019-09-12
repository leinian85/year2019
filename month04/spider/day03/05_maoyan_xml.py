from urllib import request
from fake_useragent import UserAgent
import  re
import time
import random
import csv
from lxml import etree

class spider_movie:
    movies = []
    def __init__(self):
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
        info_list = etree.HTML(html)
        infoBlock = info_list.xpath('//dd')
        for info in infoBlock:
            name = info.xpath('.//p[@class ="name"]/a/text()')[0]
            star = info.xpath('.//p[@class="star"]/text()')[0].strip()[3:]

            time = info.xpath('.//p[@class ="releasetime"]/text()')[0][5:15]

            movie = [name, star, time]
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

    def write_html(self):
        for page in range(1,3):
            url = self.get_url(page)
            print(url)
            html = self.get_html(url)
            self.get_info(html)
            time.sleep(random.randint(1,3))
        self.save_csv_rows(spider_movie.movies)

sm = spider_movie()
sm.write_html()