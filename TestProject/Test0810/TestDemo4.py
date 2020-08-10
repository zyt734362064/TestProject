import os

from selenium import webdriver
import time

driver = webdriver.Chrome()
file_path ='file:///' + os.path.abspath("E:/Test_Code/selenium2html/drop_down.html")
driver.get(file_path)
driver.maximize_window()
#Xpath 定位
#driver.find_element_by_xpath("//*[@id='ShippingMethod']/option[4]").click()
#options = driver.find_elements_by_tag_name("option")

#循环定位
#for option in options:
#    if option.get_attribute("value") == '9.03':
#        option.click()

#数组下标定位
options = driver.find_elements_by_tag_name("option")
options[3].click()

time.sleep(5)
driver.quit()