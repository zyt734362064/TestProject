#跳转页面框架
import os

from selenium import webdriver
import time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath("E:/Test_Code/selenium2html/frame.html")
driver.get(file_path)
driver.maximize_window()
#从默认页面跳转到 f2 页面
driver.switch_to.frame("f1")
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("徐睿知")
driver.find_element_by_id("su").click()
time.sleep(6)
driver.switch_to.default_content()
driver.switch_to.frame("f1")
driver.find_element_by_link_text("click").click()

time.sleep(5)
driver.quit()