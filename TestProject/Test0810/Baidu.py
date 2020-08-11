import os
import unittest
from selenium import webdriver
import time
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
class Baidu1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.driver.maximize_window()
        self.verificationErrors=[]
        self.accept_next_alert = True
        print("------setUp--------")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
        print("------tearDown--------")

    @unittest.skip("skipping")
    def test_hao(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("hao123").click()
        time.sleep(6)
        print("------hao123--------")



    def test_baiDuSearch(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertTrue("12" == "3",msg="not equal!")
        except:
            self.saveScreenShot(driver,"baiDu.png")

        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"虽然是精神病但没关系")
        driver.find_element_by_id("su").click()
        time.sleep(6)
        self.assertEqual("虽然是精神病但没关系_百度搜索", driver.title, msg="not equal!")
        time.sleep(6)
        print("------baiDu--------")

    def saveScreenShot(self, driver, file_name):
        if not os.path.exists("./errorImage"):
            os.makedirs("./errorImage")
        now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        # print("---------------------")
        # print(time.time())
        # print(time.localtime(time.ti0me()))
        # print(now)
        driver.get_screenshot_as_file("./errorImage/" + now + "-" + file_name)
        time.sleep()

    if __name__=="__main__":
        unittest.main()

