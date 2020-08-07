from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.maximize_window()

#获取文本中的内容
#text = driver.find_element_by_id("s-bottom-layer-right").text
#print("text:" + text)

driver.find_element_by_id("kw").send_keys(u"库里")
#submit 替换 click
driver.find_element_by_id("su").submit()
#固定等待
#time.sleep(8)

#只能等待
driver.implicitly_wait(8)
#driver.find_element_by_id("su").click()
driver.find_element_by_link_text("库里(金州勇士队后卫斯蒂芬·库里)_百度百科").click()
time.sleep(5)

#打印 title
title = driver.title
print(title)

#打印 url

url = driver.current_url
print(url)

#清除搜索框里的内容
#driver.find_element_by_id("kw").clear()
#driver.find_element_by_id("kw").send_keys("WNBA")
#driver.find_element_by_id("su").submit()
time.sleep(6)
driver.quit()