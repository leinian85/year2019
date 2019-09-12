import requests
from fake_useragent import UserAgent
from urllib import parse
import re
import os
import time
import random


class BaiduImgs:
    def __init__(self):
        self.baseurl = "https://image.baidu.com/search/index?tn=baiduimage&"
        self.url = ""
        self.imgList = []
        self.set_headers()

    def set_headers(self):
        ua = UserAgent()
        self.headers = {"User-Agent": ua.random}

    def set_url(self, name):
        params = {"word": name}
        sel = parse.urlencode(params)
        self.url = self.baseurl + sel

    def get_html(self, url):
        return requests.get(url, self.headers).text

    def set_img(self, html):
        pattern = re.compile('"middleURL":"(.*?)"', re.S)
        imgs = pattern.findall(html)
        print(imgs)
        for img in imgs:
            self.imgList.append(img)

    def get_imgb(self, url):
        return requests.get(url, self.headers).content

    def save_img(self, name, count):
        dirName = name + "_img"
        if not os.path.exists(dirName):
            os.mkdir(dirName)
        num = 0
        for img in self.imgList:
            num += 1
            fileName = dirName + '/' + str(num) + "." + img.split(".")[-1]
            with open(fileName, 'wb') as f:
                f.write(self.get_imgb(img))
                print("正在下载第{}张".format(num))
                time.sleep(random.randint(1, 3))
            if num == count:
                break

    def main(self, name, count):
        self.set_url(name)
        html = self.get_html(self.url)
        self.set_img(html)
        self.save_img(name, count)


bi = BaiduImgs()
bi.main('七龙珠', 10)
