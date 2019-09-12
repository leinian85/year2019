import requests
from fake_useragent import UserAgent

url = "http://b-ssl.duitang.com/uploads/item/201605/08/20160508194812_XAvds.jpeg"

ua = UserAgent()
headers = {"User-Agent":ua.random}
res = requests.get(url,headers)
with open("1.jpg",'wb') as f:
    f.write(res.content)


res = requests.get(url,headers).content.decode()
print(res.codeing)