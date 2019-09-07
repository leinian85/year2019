from urllib import request
from urllib import parse
import random
import time
from fake_useragent import UserAgent
import re


class TiebaSpider:
    def __init__(self):
        self.url = "http://tieba.baidu.com/f?kw={}&pn={}"

    def set_headers(self):
        us = UserAgent()
        self.headers = {"User-Agent":us.random}

    # 获取响应内容
    def get_page(self, url):
        self.set_headers()
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode()
        return html

    # 解析,提取数据
    def parse_page(self, name):
        return request.quote(name)

    # 保存数据
    def write_page(self, filename, html):
        with open(filename, 'w') as f:
            f.write(html)

    def run(self, name, start, end):
        for page in range(start, end + 1):
            url = self.url.format(self.parse_page(name), (page - 1) * 50)
            filename = name + "_" + str(page) + ".html"
            html = self.get_page(url)
            print(url)
            # imgs = self.get_imgs(html)
            self.write_page(filename, html)
            print("第{}页抓取成功".format(page))
            time.sleep(random.randint(1, 3))

    def get_imgs(self, html):
        pattern = re.compile("",re.S)


if __name__ == "__main__""":
    begin = time.time()
    spider = TiebaSpider()
    spider.run("赵丽颖", 1, 3)
    stop = time.time()
    print("执行时间%.2f" % (stop - begin))
