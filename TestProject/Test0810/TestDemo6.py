import os

from selenium import webdriver
import time

driver = webdriver.Chrome()
file_path ='file:///' + os.path.abspath("E:/Test_Code/selenium2html/alert.html")
driver.get(file_path)
driver.maximize_window()

driver.find_element_by_id("show_modal").click()
time.sleep(6)
div1 = driver.find_element_by_class_name("modal-body")
driver.find_element_by_link_text("click me").click()
time.sleep(5)
div2 = driver.find_element_by_class_name("modal-footer")
buttons = div2.find_elements_by_tag_name("button")
buttons[0].click()



time.sleep(8)
driver.quit()