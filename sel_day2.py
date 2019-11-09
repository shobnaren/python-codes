# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://live.demoguru99.com/")
        driver.find_element_by_link_text("MOBILE").click()

        # get price of Sony Experia

        # get all items in the list (ul and li)
        _class_name = "products-grid"
        _xpath = "//ul[contains(@class, '{}')]/li".format(_class_name)
        _list = driver.find_elements_by_xpath(_xpath)

        mobile_name = "Sony Xperia" # can be parameterized 
        for _x in _list:
            x = _x.find_element_by_xpath("//a[contains(@title,'{}')]".format(mobile_name))
            # under a title check for it matches to mobile_name
            # if x.get_attribute("title") in mobile_name:
            if x:
                # when matches get the price on the page
                p = _x.find_element_by_xpath('//span[contains(@id,"product-price")]').text
                print("-"*50)
                print("price of Xperia = {}".format(p))
                print("-"*50)
                # and click the same href to go down the details page
                _x.click()
            else:
                print("unable to find the hyperlink for mobile")

        # On the details page look for price under "<span>" tag
        _xpath = '//span[contains(@class,"price")]'
        price = driver.find_element_by_xpath(_xpath).text
        print(price)
        self.assertEqual(p,price)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
