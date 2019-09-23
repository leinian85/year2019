import json
import requests
from fake_useragent import  UserAgent

class doubanSpider:
    def __init__(self):
        self.url = ""

    def set_headers(self):
        ua = UserAgent()
        headers = ("User-agent",ua.random)

    def get_html(self):
        html = requests.get(self.url,headers = self.headers).text
        return html

    def parese_page(self,url):
        html_json = self.get_html(url)
        html_py = json.loads(html_json)