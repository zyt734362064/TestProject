from selenium.webdriver.common.keys import Keys

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:88/biz/user-login-L2Jpei8=.html")

driver.maximize_window()
#输入用户名
driver.find_element_by_name("account").send_keys("admin")
#切换光标
driver.find_element_by_name("account").send_keys(Keys.TAB)
time.sleep(4)
#输入密码
driver.find_element_by_name("password").send_keys("YCzyt123")
#输入ENTER 键登录
driver.find_element_by_name("password").send_keys(Keys.ENTER)

time.sleep(8)
driver.quit()