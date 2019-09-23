from selenium import webdriver
import time

browser = webdriver.PhantomJS()
browser.get("http://www.baidu.com")
browser.save_screenshot('baidu.png')
time.sleep(5)
browser.quit()