import requests
url = "http://code.tarena.com.cn/AIDCode/aid1905/14_spider/"
auth = ("tarenacode","code_2014")
headers = {"User-Agent":"Mozilla/5.0"}
html = requests.get(url=url,auth = auth,headers = headers).content.decode("utf-8","ignore")
print(html)