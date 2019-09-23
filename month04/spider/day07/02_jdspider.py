from selenium import webdriver
import time

class JdSpider:
    def __init__(self):
        self.url = "https://www.jd.com/"
        self.browsder = webdriver.Chrome()
        self.books = []

    def get_html(self,key):
        self.browsder.get(self.url)
        sel = self.browsder.find_element_by_xpath('//*[@id="key"]')
        sel.send_keys(key)
        fnd = self.browsder.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
        fnd.click()
        time.sleep(3)

    def parse_html(self):
        self.browsder.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        time.sleep(3)

        li_list = self.browsder.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')

        for li in li_list:

            abook = {}
            price = li.find_element_by_xpath('.//div[@class="p-price"]').text.strip()
            title = li.find_element_by_xpath('.//div[@class="p-name"]').text.strip()
            market = li.find_element_by_xpath('.//div[@class="p-shopnum"]').text.strip()
            abook["price"] = price
            abook["title"] = title
            abook["market"] = market
            print(abook)
            self.books.append(abook)
        print(len(self.books))

    def run(self,ksy):
        self.get_html(ksy)
        self.parse_html()
        for i in range(3):
            if self.browsder.page_source.find("pn-next disable") == -1:
                self.browsder.find_element_by_class_name('pn-next').click()
                time.sleep(3)
                self.parse_html()
            else:
                break

js = JdSpider()
js.run('爬虫')