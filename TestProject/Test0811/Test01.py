from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://152.136.97.191:8080/rainbowMusic/login.html")

#登录
driver.maximize_window()
driver.find_element_by_id("user").send_keys("aaa")
driver.find_element_by_id("password").send_keys("123")
driver.find_element_by_id("submit").click()
time.sleep(3)

#上传歌曲
driver.find_element_by_link_text(u"添加歌曲").click()
driver.find_element_by_name("filename").send_keys("C:/Users/Zyt/Music/believer.mp3")
time.sleep(5)

#添加歌手名称
driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[2]/input").click()
time.sleep(8)
driver.find_element_by_name("singer").send_keys("Imagine Dragons")
driver.find_element_by_xpath("/html/body/form/div[2]/input").click()
time.sleep(8)

#删除歌曲
driver.find_element_by_xpath("//*[@id='info']/tr/td[4]/button[1]").click()
time.sleep(5)
alert = driver.switch_to.alert
alert.accept()


time.sleep(5)
driver.quit()
