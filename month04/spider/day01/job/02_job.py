from urllib import request
from fake_useragent import UserAgent
import  re
import time
import random

class spider_movie:
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
        pattern = re.compile('<dd>.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>',re.S)
        movie_infos = pattern.findall(html)

        result = ""
        for info in movie_infos:
            result += """电影名称:{}
主演:{}
上映时间:{}
****************************
""".format(info[0],info[1].strip(),info[2])
        return result

    def write_html(self):
        with open("猫眼电影.html","w") as f:
            for page in range(1,11):
                url = self.get_url(page)
                print(url)
                html = self.get_html(url)
                movie_info = "猫眼电影-第{}页\n".format(page) + self.get_info(html)
                f.write(movie_info)
                time.sleep(random.randint(1,3))

sm = spider_movie()
sm.write_html()