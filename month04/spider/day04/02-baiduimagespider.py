import requests
from lxml import etree
import time
import random
from urllib import parse


class TiebaImageSpider:
    def __init__(self):
        self.url = "http://tieba.baidu.com/f?kw={}&pn={}"
        self.headers = {"User-Agent": ""}

    def get_html(self, url):
        res = requests.get(url=url, headers=self.headers)
        html = res.content

        return html

    def xpath_func(self, html, xpath_dbs):
        parse_obj = etree.HTML(html)
        r_list = parse_obj.xpath(xpath_dbs)

        return r_list

    def save_img(self, img_link, filename):
        html = self.get_html(img_link)
        with open("img/"+filename, 'wb') as f:
            f.write(html)

    def get_img(self, tlink):
        html = self.get_html(tlink).decode("utf-8","ignore")
        xpath_dbs = '//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src'
        img_link_list = self.xpath_func(html, xpath_dbs)
        i = 0
        for img_link in img_link_list:
            i += 1
            filename = str(i)+"."+img_link.split(".")[-1]
            # print(img_link)
            self.save_img(img_link,filename)
        print("下载成功!")

    def parse_html(self, url):
        # 1.先提取帖子链接
        one_html = self.get_html(url).decode()
        xpath_dbs = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
        tlink_list = self.xpath_func(one_html, xpath_dbs)
        for tlink in tlink_list:
            tlink = "http://tieba.baidu.com" + tlink
            self.get_img(tlink)

    def run(self, name, start, end):
        name = parse.quote(name)
        for page in range(start, end + 1):
            pn = (page - 1) * 50
            url = self.url.format(name, pn)
            self.parse_html(url)
            time.sleep(random.randint(1,3))


tb = TiebaImageSpider()
tb.run("赵丽颖", 1, 1)
