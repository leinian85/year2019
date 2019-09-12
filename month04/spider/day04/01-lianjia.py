# 爬取链家二手房
import requests
from fake_useragent import UserAgent
from lxml import etree
import time,random,csv


class Lianjia:
    def __init__(self):
        self.baseUrl = ""

    def set_hesders(self):
        ua = UserAgent()
        self.headers = {"User-Agent": ua.random}

    def set_baseurl(self, page):
        if page == 1:
            self.baseUrl = "https://wh.lianjia.com/ershoufang/"
        else:
            self.baseUrl = "https://wh.lianjia.com/ershoufang/pg{}/".format(page)

    def get_html(self):
        for i in range(3):
            try:
                html = requests.get(url=self.baseUrl, headers=self.headers,timeout=5).content.decode('utf-8','ignore')
                return html
            except:
                pass

    def get_str(self,text,str):
        info = text.xpath(str)
        return info[0] if info else None

    def get_info(self,html):
        pattern = etree.HTML(html)
        fy_list = pattern.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
        # res = pattern.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGCLICKDATA"]')
        with open("lianjiaershou.csv",'a') as f:
            writer = csv.writer(f)
            f_list = []
            for fy in fy_list:
                item = {}
                item["url"] = self.get_str(fy,'./a[@class="noresultRecommend img LOGCLICKDATA"]/@href')
                item["title"] = self.get_str(fy,'.//div[@class="title"]/a/text()')
                item["address"] = self.get_str(fy,'.//div[@class="address"]//a/text()')
                item["houseInfo"] = self.get_str(fy,'.//div[@class="houseInfo"]/a/text()')
                item["adressinfo"] = self.get_str(fy,'.//div[@class="address"]/div/text()').split("|")[1:]
                if len(item["adressinfo"]) == 4:
                    item["house_type"] = item["adressinfo"][0].strip()
                    item["size"] = item["adressinfo"][1].strip()[:-2]
                    item["towards"] = item["adressinfo"][2].strip()
                    item["fitment"] = item["adressinfo"][3].strip()
                else:
                    item["house_type"] = None
                    item["size"] = None
                    item["towards"] = None
                    item["fitment"] = None

                item["flood"] = self.get_str(fy,'.//div[@class="flood"]/div/text()').split("-")[0].strip()
                item["positionInfo"] = self.get_str(fy,'.//div[@class="positionInfo"]/a/text()')
                item["totalPrice"] = float(self.get_str(fy,'.//div[@class="totalPrice"]/span/text()'))*10000
                item["unitPrice"] = self.get_str(fy,'.//div[@class="unitPrice"]/span/text()')[2:-4]
                fy_one = (item["title"],item["address"],item["houseInfo"],item["house_type"],item["size"],item["towards"],item["fitment"],item["flood"],item["positionInfo"],item["totalPrice"],item["unitPrice"],item["url"])
                f_list.append(fy_one)
            # print(fy_list)
            writer.writerows(f_list)


    def main(self,start,end):
        for page in range(start,end+1):
            self.set_baseurl(page)
            self.set_hesders()
            html = self.get_html()
            if html:
                self.get_info(html)
            print("第{}页提取完成!".format(page))
            time.sleep(random.randint(1,3))

lj = Lianjia()
lj.main(1,100)
