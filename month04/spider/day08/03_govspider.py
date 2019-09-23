from selenium import webdriver
import pymysql


class GovSpider:
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.db = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='123456',
            database='blog',
            port=3306,
            charset='utf8'
        )
        self.cursor = self.db.cursor()
        self.browser = webdriver.Chrome()
        self.province = []  # 省
        self.city = [] # 市
        self.county = [] # 区

    def get_data(self):
        self.browser.get(self.url)
        xpath_dbs = '//td[@class="arlisttd"]/a[contains(@title,"行政区划代码")]'
        a = self.browser.find_element_by_xpath(xpath_dbs)
        href = a.get_attribute("href")

        if href:
            a.click()
            self.set_code()

    def set_code(self):
        # 1.切换句柄
        all_handles = self.browser.window_handles
        self.browser.switch_to.window(all_handles[1])

        tr_list = self.browser.find_elements_by_xpath('//tr[@height="19"]')

        self.del_mysql()

        for tr in tr_list:
            code = tr.find_element_by_xpath('./td[2]').text.strip()
            name = tr.find_element_by_xpath('./td[3]').text.strip()
            # print(code,name)
            if code.endswith('0000'):
                self.province.append((name,code))
                if name in ("北京市","天津市","上海市","重庆市"):
                    self.city.append((name,code,code))
            elif code.endswith('00'):
                self.city.append((name,code,code[:2]+'0000'))
            else:
                if code[:2] in ("11","12","31","50"):
                    self.county.append((name,code,code[:2]+'0000'))
                else:
                    self.county.append((name,code,code[:4]+'00'))
        print("数据抓取完成")
        self.save_mysql()
        print("数据保存完成")

    def del_mysql(self):
        sql = "delete from province"
        self.cursor.execute(sql)
        sql = "delete from city"
        self.cursor.execute(sql)
        sql = "delete from county"
        self.cursor.execute(sql)
        self.db.commit()

    def save_mysql(self):
        sql = "insert into province(p_name,p_code) values (%s,%s)"
        self.cursor.executemany(sql,self.province)
        sql = "insert into city(c_name,c_code,c_father_code) values (%s,%s,%s)"
        self.cursor.executemany(sql, self.city)
        sql = "insert into county(x_name,x_code,x_father_code) values (%s,%s,%s)"
        self.cursor.executemany(sql, self.county)
        self.db.commit()

gs = GovSpider()
gs.get_data()
