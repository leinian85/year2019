from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
set_node = browser.find_element_by_xpath('//*[@id="u1"]/a[8]')

mouse_obj = ActionChains(browser)
mouse_obj.move_to_element(set_node)
mouse_obj.perform()

browser.find_element_by_link_text('高级搜索').click()
# browser.quit()