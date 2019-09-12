from urllib import request
from fake_useragent import UserAgent
import time
import random
import re
import os


class movie:
    def __init__(self):
        self.url1 = []
        self.url2 = []
        self.movies = []
        self.imgslit = []
        pass

    def get_urllvele1(self, page):
        for p in range(1, page + 1):
            if p == 1:
                self.url1.append("https://maoyan.com/board/4")
            else:
                self.url1.append("https://maoyan.com/board/4?offset=" + str((p - 1) * 10))

    def set_headers(self):
        us = UserAgent()
        self.headers = {"User-Agent": us.random}

    def gethtml1(self, url1):
        url = request.Request(url=url1, headers=self.headers)
        req = request.urlopen(url)
        return req.read().decode()

    def get_url2(self, html):
        pattern = re.compile('<dd>.*?<a href="(.*?)".*?</dd>', re.S)
        urllist = pattern.findall(html)
        self.url2.append(['https://maoyan.com'+url for url in urllist])

    def __get_html2(self,url):
        print(url)
        url = request.Request(url=url,headers=self.headers)
        req = request.urlopen(url)
        return req.read().decode()

    def get_info2(self,url):
        movie = {}
        html = self.__get_html2(url)
        pattern = re.compile('<h3 class="name">(.*?)</h3>',re.S)
        name = pattern.findall(html)
        # print("name:",name)
        movie["name"] = name[0]
        pattern = re.compile('<div class="comment-content">(.*?)</div>',re.S)
        context = pattern.findall(html)
        # print(context)
        movie["context"] = context
        imgs = self.__save_imgs(html)
        movie["imgs"] = imgs
        self.movies.append(movie)

    def __save_imgs(self,html):
        pattern = re.compile('<img class="default-img" data-act="movie-img-click" data-src="(.*?)" alt="">',re.S)
        return pattern.findall(html)


    def save_movies(self):
        with open("movis.html","a") as f:
            f.write(str(self.movies))

    def __save_files(self,name,imgs,count):
        if not os.path.exists(name):
            os.mkdir(name)

        counti = 0
        for img in imgs:
            counti += 1
            filename = img.split("@")[0].split("/")[-1]
            file = name + '/' + filename

            iurl = request.Request(url=img,headers=self.headers)
            phont = request.urlopen(iurl)
            with open(file,'wb') as i:
                i.write(phont.read())
            if counti > count:
                break
            time.sleep(random.randint(1, 3))

    def save_photos(self):
        for movie in self.movies:
            name = movie["name"]
            imgs = movie["imgs"]

            self.__save_files(name, imgs,10)




mv = movie()
mv.get_urllvele1(1)
mv.set_headers()
for url in mv.url1:
    html = mv.gethtml1(url)
    mv.get_url2(html)
    time.sleep(random.randint(1, 3))

# print(mv.url2)
for url2 in mv.url2:
    for aurl in url2:
        mv.get_info2(aurl)
        mv.save_movies()
        time.sleep(random.randint(1, 3))

mv.save_photos()
