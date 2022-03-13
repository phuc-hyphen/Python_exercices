# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re

from selenium.webdriver.support.wait import WebDriverWait


class Addemployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('C:\Formation\Drivers\chromedriver.exe')
        cls.driver.implicitly_wait(5)
        cls.base_url = "http://localhost/orangehrm/symfony/web/index.php/auth/login"
        cls.verificationErrors = []
        cls.accept_next_alert = True
        cls.latence=2

    def wait_for_element(self, by, locator):
        # Implicite wait : wait for element to be presente
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            print("Element not visible", by, locator)

    def test_a_login(self):
        driver = self.driver
        driver.get(self.base_url)
        self.wait_for_element(By.ID, "txtUsername")
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "txtUsername"): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        driver.find_element_by_id("txtUsername").click()
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("frmLogin").click()
        driver.find_element_by_id("txtPassword").click()
        driver.find_element_by_id("txtPassword").send_keys("Test.IT$2021")
        driver.find_element_by_id("btnLogin").click()
        self.assertEqual("Bienvenue Hassan", driver.find_element_by_id("welcome").text)
        driver.get_screenshot_as_file('C:\\Formation\\tmp\\login.png')

    def test_b_addemployee(self):
        driver = self.driver
        # driver.get(self.base_url)
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        time.sleep(self.latence)
        # self.wait_for_element(By.ID, "txtUsername")
        # driver.find_element_by_id("menu_pim_viewPimModule").click()
        driver.find_element_by_id("menu_pim_addEmployee").click()

        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys("Hello")

        driver.find_element_by_id("middleName").clear()
        driver.find_element_by_id("middleName").send_keys("the")

        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys("world")

        driver.find_element_by_id("frmAddEmp").submit()
        driver.find_element_by_id("btnSave").click()

        driver.find_element_by_id("personal_cmbMarital").click()
        Select(driver.find_element_by_id("personal_cmbMarital")).select_by_visible_text(u"Célibataire")
        driver.find_element_by_id("personal_optGender_1").click()
        driver.find_element_by_id("personal_cmbNation").click()
        Select(driver.find_element_by_id("personal_cmbNation")).select_by_visible_text(u"Français")
        driver.find_element_by_id("btnSave").click()

        driver.find_element_by_id("welcome").click()
        driver.find_element_by_link_text(u"Déconnexion").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print(cls.verificationErrors)
        # cls.assertEqual([], cls.verificationErrors)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True


if __name__ == "__main__":
    unittest.main()
