# http://tieba.baidu.com/f?kw=%E8%B5%B5%E4%B8%BD%E9%A2%96&pn=0
# http://tieba.baidu.com/f?kw=%E8%B5%B5%E4%B8%BD%E9%A2%96&pn=50

from urllib import parse
import random
import time
from urllib import request


def get_url(name, page):
    baseurl = "http://tieba.baidu.com/f?"
    params = {"kw": name, "pn": page}
    paramsb = parse.urlencode(params)
    url = baseurl + paramsb
    return url


def get_page(page):
    return (page - 1) * 50


def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
    res = request.Request(url=url, headers=headers)
    return request.urlopen(res).read().decode()


def write_html(name, start, end):
    for i in range(start, end + 1):
        page = get_page(i)
        url = get_url(name, page)
        filename = name + "_" + str(page) + ".html"
        html = get_html(url)
        with open(filename, "w") as f:
            f.write(html)





write_html("赵丽颖", 1, 3)


