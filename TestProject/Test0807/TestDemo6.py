import os

from selenium import webdriver
import time

driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath("E:/Test_Code/selenium2html/checkbox.html")
driver.get(file_path)
driver.maximize_window()
inputs = driver.find_element_by_tag_name("input")
time.sleep(15)
for input in inputs:
    if input.get_attribute('type') == "checkbox":
        input.click()
time.sleep(10)
driver.quit()
