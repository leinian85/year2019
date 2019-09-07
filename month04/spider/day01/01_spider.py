from urllib import request

url = "http://httpbin.org/get"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}

req = request.Request(url=url,headers=headers)

res = request.urlopen(req)

html = res.read().decode()

print(html)

from urllib import parse
baseurl = "https://www.baidu.com/s?"
params = {"wd":"赵丽颖","pn":"10"}
result = parse.urlencode(params)
url = baseurl + result
print(url) # https://www.baidu.com/s?wd=%E8%B5%B5%E4%B8%BD%E9%A2%96&pn=10

# 字典编码
params = {"wd":"赵丽颖","pn":"10"}
paramsb = parse.urlencode(params)
print(paramsb) #
# 字符串编码
word = "赵丽颖"
wordb = parse.quote(word)
print(wordb) #