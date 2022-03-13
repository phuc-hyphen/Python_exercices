# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AddEMplloyee(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Formation\Drivers\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://opensource-demo.orangehrmlive.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_e_mplloyee(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_xpath("//div[@id='divUsername']/span").click()
        driver.find_element_by_id("txtUsername").click()
        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").click()
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_id("menu_pim_addEmployee").click()
        driver.find_element_by_id("firstName").click()
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys("Phuc")
        driver.find_element_by_id("middleName").click()
        driver.find_element_by_id("middleName").clear()
        driver.find_element_by_id("middleName").send_keys("HUU")
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys("LE")
        driver.find_element_by_id("btnSave").click()
        driver.find_element_by_id("welcome").click()
        driver.find_element_by_link_text("Logout").click()
        driver.close()
    
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
