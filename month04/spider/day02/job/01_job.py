from fake_useragent import UserAgent
from urllib import request
from urllib import parse
import requests
import re
import os
import time
import random

class SpiderImgs():
    def __init__(self):
        self.imgs = {}
        self.baseurl = "http://image.baidu.com/search/index?tn=baiduimage&"
        self.__set_headers()

    def __set_headers(self):
        us = UserAgent()
        self.heasers = {"User-Agent":us.random}



    def __get_html(self,url):
        req = request.Request(url = url,headers = self.heasers)
        html = request.urlopen(req)
        print(html.read().decode())
        return html.read().decode()

    def __select_info(self,name):
        params = {"word":name}
        return parse.urlencode(params)

    def __get_url(self,name):
        return self.baseurl + self.__select_info(name)


    def __get_imgs(self,html,count):
        pattern = re.compile('"thumbURL":"(.*?)"',re.S)
        img_list = pattern.findall(html)[:count+1]
        return img_list

    def __set_imgs(self, name,count):
        url = self.__get_url(name)
        html = self.__get_html(url)
        # with open("1.text","w") as f:
        #     f.write(html)
        print(url)
        url_imgs = self.__get_imgs(html,count)
        print("url_imgs:",url_imgs)
        self.imgs[name] = url_imgs

    def save_imgs(self,name,urls):
        if not os.path.exists(name):
            os.mkdir(name)

        for url in urls:
            filename = name + '/'


    def main(self, name,count):
        self.__set_imgs(name,count)
        print(self.imgs[name])
        # self.save_imgs(name,self.imgs[name])

sp = SpiderImgs()
sp.main("赵丽颖",10)