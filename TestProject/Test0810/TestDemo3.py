import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

driver = webdriver.Chrome()
file_path ='file:///' + os.path.abspath("E:/Test_Code/selenium2html/level_locate.html")
driver.get(file_path)

driver.find_element_by_link_text("Link1").click()
button = driver.find_element_by_link_text("Another action")

#讲述表移动到目标元素
ActionChains(driver).move_to_element(button).perform()


time.sleep(5)
driver.quit()