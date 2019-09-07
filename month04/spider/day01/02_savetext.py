from urllib import request
from urllib import parse

def get_url(word):
    baseurl = "https://www.baidu.com/s?"

    # 编码 + 拼接
    params = {"wd":word}
    request = parse.urlencode(params)
    return baseurl + request

def writh_html(word):
    url = get_url(word)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
    req = request.Request(url=url,headers = headers)
    res = request.urlopen(req)
    html = res.read().decode()
    filename = word + ".html"
    with open(filename,"w",encoding="utf-8") as f:
        f.write(html)

writh_html("赵丽颖")
