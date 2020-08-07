from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("徐睿知")
su1 = driver.find_element_by_id("su")
#右击
ActionChains(driver).context_click(su1).perform()
time.sleep(5)
#双击
ActionChains(driver).double_click(su1).perform()

#移动鼠标
title = driver.find_element_by_id("su")
driver.implicitly_wait(10)
target = driver.find_element_by_link_text("徐睿知_百度百科")

ActionChains(driver).drag_and_drop(title,target).perform()

time.sleep(8)
driver.quit()