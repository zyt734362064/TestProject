import os

from selenium import webdriver
import time

driver = webdriver.Chrome()
file_path ='file:///' + os.path.abspath("E:/Test_Code/selenium2html/alert.html")
driver.get(file_path)
driver.maximize_window()

driver.find_element_by_id("tooltip").click()
time.sleep(8)
alert = driver.switch_to.alert
text = alert.text
print("text=" + text)
alert.accept()

time.sleep(5)
driver.quit()