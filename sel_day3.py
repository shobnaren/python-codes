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
        _class_name = "products-grid"
        _xpath = "//ul[contains(@class, '{}')]/li".format(_class_name)
        _list = driver.find_elements_by_xpath(_xpath)
        # another approach
        # items = _list.find_elements_by_css_selector("li a")
        # title_list = [x.get_attribute("title") for x in _list]
        mobile_name = "Sony Xperia"
        for _x in _list:
            x = _x.find_element_by_tag_name('a')
            if x.get_attribute("title") in mobile_name:
                _xpath = '//button[contains(@title,"Add to Cart")]'
                we = _x.find_element_by_xpath(_xpath)
                we.click()
                #time.sleep(3)
                break;

        _xpath = '//input[contains(@title, "Qty")]' # name is empty for the text box
        we = driver.find_element_by_xpath(_xpath)
        print(dir(we))
        we.clear()
        we.send_keys("1000")

        _xpath = '//button[[contains(@title, "Update Shopping Cart")] and [contains(@value,"update_qty")]]'
        _xpath = '//button[contains(@title, "Update Shopping Cart")]'
        we_l = driver.find_elements_by_xpath(_xpath)
        for we in we_l:
            print(we.is_enabled())
            if we.is_displayed():
                print("click the one displayed")
                we.click()

        time.sleep(3)
        _err_msg = "The maximum quantity allowed for purchase is 500"
        _xpath = '//p[contains(@class, "item-msg")]'
        we = driver.find_element_by_xpath(_xpath)
        err_msg = we.text
        print(dir(we))
        print(err_msg)
        self.assertEqual(err_msg, _err_msg)
        """
        # driver.find_element_by_id("product-collection-image-1").click()
        # find element by xpath
        _xpath = '//span[contains(@class,"price")]'
        price = driver.find_element_by_xpath(_xpath).text
        print(price)
        """
    
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
