from urllib import request
from fake_useragent import UserAgent
import  re
import time
import random
import csv
import pymongo

class spider_movie:
    movies = []
    def __init__(self):
        self.conn = pymongo.MongoClient("localhost",27017)
        self.db = self.conn["maoyandb"]
        self.myset = self.db["filmtab"]
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
            movie = {"name":info[0],"star":info[1].strip()[3:],"time":info[2][5:15]}
            spider_movie.movies.append(movie)

    def save_mongodb(self,file):
        self.myset.insert_many(file)

    def save_mongo(self,file):
        for item in file:
            self.myset.insert_one(item)

    def write_html(self):
        for page in range(1,3):
            url = self.get_url(page)
            print(url)
            html = self.get_html(url)
            self.get_info(html)
            time.sleep(random.randint(1,3))
        # self.save_mongodb(self.movies)
        self.save_mongo(self.movies)

sm = spider_movie()
sm.write_html()