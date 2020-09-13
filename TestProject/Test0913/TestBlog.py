from selenium import webdriver
import time

driver = webdriver.Chrome()
time.sleep(3)
driver.get("http://152.136.97.191:8080/blog_2/login.html")

time.sleep(3)

driver.maximize_window()
driver.find_element_by_name("name").send_keys("aaa")
driver.find_element_by_name("password").send_keys("123")
driver.find_element_by_xpath("/html/body/form/input[3]").click()
time.sleep(3)
driver.find_element_by_link_text("点击这里进行跳转").click()
time.sleep(5)
driver.find_element_by_name("title").send_keys("测试文章标题")
driver.find_element_by_name("content").send_keys("测试输入文章内容")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[5]/form/input[2]").click()
time.sleep(5)
driver.find_element_by_link_text("点击这里进行跳转").click()
time.sleep(5)
driver.find_element_by_link_text("测试文章标题").click()
time.sleep(5)

driver.quit()