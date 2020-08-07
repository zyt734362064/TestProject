from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("徐睿知")
driver.find_element_by_id("su").click()
#复制
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(5)

#剪切
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(5)

#复制
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')

time.sleep(5)
driver.quit()