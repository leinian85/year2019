import requests
from fake_useragent import UserAgent

url = "http://www.baidu.com"
ua = UserAgent()

headers = {"User-Agent":ua.random}

res = requests.get(url,headers)
# encoding 字符编码
res.encoding = "utf-8"
# text 响应内容 字符串
html = res.text
# content 响应内容 字节串
htmlb = res.content
# status_code 响应码
code = res.status_code
# 返回真实数据的地址
url = res.url

print(htmlb)