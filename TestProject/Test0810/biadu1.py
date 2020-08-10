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
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"虽然是精神病但没关系")
        driver.find_element_by_id("su").click()
        time.sleep(6)
        #self.assertEqual("虽然是精神病但没关系_百度搜索",driver.title,msg="not equal!")
        self.assertTrue(1+2 == 4,msg="not True!")
        time.sleep(6)

        print("------baiDu--------")


    if __name__=="__main__":
        unittest.main()