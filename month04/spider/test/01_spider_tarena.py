import requests
from fake_useragent import UserAgent
import os
from lxml import etree
import time
import random


class TarenaSpider:
    def __init__(self,dir,ignore = []):
        self.classNo = "1905"
        self.auth = ("tarenacode", "code_2014")
        self.dir = dir
        self.ignore = ignore
        self.ua = UserAgent()
        self.new_file = []

    def get_html(self, url):
        print("url-dir:",url)
        headers = {"User-Agent": self.ua.random}
        # proxies = {
        #     "http":"http://27.204.112.20:9999",
        #     "https":"http://27.204.112.20:9999"
        # }
        html = requests.get(url=url, auth=self.auth, headers=headers,
                            # proxies = proxies
                            )
        return html

    def go_next_dir(self, url,if_dir):
        if not if_dir:
            self.download(url)
            return

        html = self.get_html(url).content.decode("utf-8","ignore")
        r_obj = etree.HTML(html)
        r_list = r_obj.xpath("//a/@href")
        for urlone in r_list:
            if urlone in self.ignore:
                continue

            dir_one = url + urlone

            # url = "http://code.tarena.com.cn/AIDCode/aid1905/14_spider/"
            # 获取上级目录 AIDCode/aid1905/14_spider/
            is_dir = False
            if dir_one.endswith("/"):
                dir = self.dir + dir_one[26:]
                is_dir = True
            else:
                dir = self.dir + "/".join(dir_one[26:].split("/")[:-2])
                is_dir = False

            if not os.path.exists(dir):
                # os.mkdir(dir)
                os.makedirs(dir)

            self.go_next_dir(dir_one,is_dir)
            time.sleep(random.randint(1, 3))


    def download(self,url):
        print("url-file:",url)
        filename = self.dir + url[26:]
        if os.path.exists(filename):
            print("{} 已经存在".format(filename))
            return
        res = self.get_html(url).content
        with open(filename,"wb") as f:
            f.write(res)
            self.new_file.append(url)
            print("{}下载完成".format(filename))





baseurl = "http://code.tarena.com.cn/AIDCode/aid1905/14_spider/"
# 设置下载目录
downdir = "/home/tarena/1905/"
# 设置忽略文件夹
ignore = ["../"]
ts = TarenaSpider(downdir,ignore)
ts.go_next_dir(baseurl,True)
print("全部下载完成,文件位置:{}".format(downdir))
print("新增文件{}个:".format(len(ts.new_file)))
for item in ts.new_file:
    print(item)