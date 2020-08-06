 # coding = utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(8)

# id 的定位
#driver.find_element_by_id("kw").send_keys("三十而已")
#driver.find_element_by_id("su").click()

#通过 name 定位
#driver.find_element_by_name("wd").send_keys("三十而已")
#driver.find_element_by_id("su").click()

#class name 的定位
#driver.find_element_by_class_name("s_ipt").send_keys("三十而已")
#driver.find_element_by_id("su").click()

#link text 定位
#driver.find_element_by_link_text(u"视频").click()

#tag name 定位
#driver.find_element_by_tag_name("")

#Xpath 定位
driver.find_element_by_xpath("//*[@id='kw']").send_keys("CBA")
driver.find_element_by_xpath("//*[@id='su']").click()


time.sleep(6)
driver.quit()