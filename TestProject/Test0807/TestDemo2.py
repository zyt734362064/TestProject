from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

#浏览器的放大
driver.maximize_window()
time.sleep(5)
#浏览器的缩小
driver.minimize_window()
time.sleep(5)

#设置浏览器的宽和高
driver.set_window_size(400,800)
time.sleep(5)

driver.find_element_by_id("kw").send_keys(u"库里")
driver.find_element_by_id("su").submit()
time.sleep(5)

#设置浏览器的滚动条到最底端
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(5)
#设置浏览器的滚动条到最顶端
js1 = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(5)

driver.quit()
