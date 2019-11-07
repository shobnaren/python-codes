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
        driver.get("http://live.demoguru99.com/index.php/")
        driver.find_element_by_link_text("MOBILE").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sort By'])[1]/following::select[1]").click()
        Select(driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sort By'])[1]/following::select[1]")).select_by_visible_text("Name")
        # Best approach is to use xpath though we can use by_class_name / by_css_selector etc...
        _class_name = "products-grid"
        _xpath = "//ul[contains(@class, '{}')]/li/a".format(_class_name)
        _list = driver.find_elements_by_xpath(_xpath)
        # another approach
        # items = _list.find_elements_by_css_selector("li a")
        title_list = [x.get_attribute("title") for x in _list]
        print(title_list)
        if sorted(title_list) == title_list:
            # On the browser the name is used to sort and verify
            # We take the same and do the comparison against PYTHON sorted
            print("SUCCESS {}".format(title_list))
            return True
        else:
            return False
    
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
