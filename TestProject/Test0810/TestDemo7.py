import os

from selenium import webdriver
import time

driver = webdriver.Chrome()
file_path ='file:///' + os.path.abspath("E:/Test_Code/selenium2html/upload.html")
driver.get(file_path)
driver.maximize_window()
time.sleep(3)
#定位上传文件按钮
driver.find_element_by_tag_name("input").send_keys("C:/Users/Zyt/Music/屋顶.mp3")



time.sleep(8)
driver.quit()