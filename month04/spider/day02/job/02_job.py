from fake_useragent import UserAgent
from urllib import request
import re
import time
import random


class Movie:
    def __init__(self):
        self.url2 = []
        self.movie_info = []

    def set_baseurl(self, page):
        if page == 1:
            self.baseurl1 = "https://www.dytt8.net/html/gndy/dyzz/index.html"
        else:
            self.baseurl1 = "https://www.dytt8.net/html/gndy/dyzz/list_23_" + page + ".html"

    def set_headers(self):
        ua = UserAgent()
        self.headers = {"User-Agent": ua.random}

    def get_html_level(self, url):
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode("gb2312", "ignore")
        return html

    def set_url2(self, html):
        headurl = "https://www.dytt8.net"
        pattern = re.compile('<table width="100%".*?<a href="(.*?)" class="ulink">.*?</table>', re.S)
        urls = pattern.findall(html)
        for url in urls:
            self.url2.append(headurl + url)

    def set_page_info(self, html):
        pattern = re.compile('<div class="title_all"><h1><font.*?《(.*?)》.*?<td style="WORD-WRAP: break-word".*?<a '
                             'href="(.*?)">', re.S)
        res = pattern.findall(html)
        # print(res)
        name = res[0][0]
        download = res[0][1]
        self.movie_info.append({"name": name, "download": download})
        return name

    def main(self, start=1, end=1):
        self.set_headers()
        # 获取二级页面的url
        for page in range(start, end + 1):
            self.set_baseurl(page)
            html = self.get_html_level(self.baseurl1)

            self.set_url2(html)
            time.sleep(random.randint(1, 3))
            print("二级页面url抓取完成.")

        for url in self.url2:
            html = self.get_html_level(url)
            name = self.set_page_info(html)
            print("第{}个: {} 抓取完成 url = {}".format(self.url2.index(url) + 1, name,url))
            time.sleep(random.randint(1, 3))


        for item in self.movie_info:
            print(item)


mv = Movie()
mv.main()
