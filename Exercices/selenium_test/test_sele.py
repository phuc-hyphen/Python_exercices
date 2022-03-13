# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
import unittest, time

class GestionEmploye(unittest.TestCase):
    # this method is run before all tests
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Formation\\drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.base_url = "http://localhost/orangehrm"
        cls.admin_pwd = "Test.IT$2021"
        cls.verificationErrors = []
        cls.accept_next_alert = True
        cls.employeeId = "8888"
        cls.lastName= "IMHAH"
        cls.firstName = "Hassan"
        cls.latence = 2

    def wait_for_element(self, by, locator):
        # Implicite wait : wait for element to be presente
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            print ("Element not visible",by, locator)

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
        # type username
        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("admin")
        # to adjust test run change latence (in seconds)
        time.sleep(self.latence)
        # type password
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys(self.admin_pwd)
        time.sleep(self.latence)
        # click login
        driver.find_element_by_id("btnLogin").click()
        time.sleep(self.latence)
        self.assertEqual("Bienvenue Hassan", driver.find_element_by_id("welcome").text)
        # Take screen shot and save it to c:/formation/tmp....
        driver.get_screenshot_as_file('C:\\Formation\\tmp\\login.png')

    def test_b_change_localization(self):
        driver = self.driver
        self.wait_for_element(By.ID, "menu_admin_viewAdminModule")
        driver.find_element_by_id("menu_admin_viewAdminModule").click()
        time.sleep(self.latence)
        driver.find_element_by_id("menu_admin_Configuration").click()
        time.sleep(self.latence)
        driver.find_element_by_id("menu_admin_localization").click()
        time.sleep(self.latence)
        lang = driver.find_element_by_id("localization_dafault_language").get_attribute("value")
        # if localization already in english, do nothing
        # if not set localization to english, otherwise some text verifications will fail
        if (lang == "en_US"):
            pass
        else:
            driver.find_element_by_id("btnSave").click()
            Select(driver.find_element_by_id("localization_dafault_language")).select_by_value("en_US")
            driver.find_element_by_id("btnSave").click()
        # Take screen shot and save it to c:/formation/tmp....
        driver.get_screenshot_as_file('C:\\Formation\\tmp\\change_localization.png')

    def test_c_add_employee(self):
        driver = self.driver
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        time.sleep(self.latence)
        driver.find_element_by_id("menu_pim_addEmployee").click()
        time.sleep(self.latence)
        # type last name
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys(self.lastName)
        time.sleep(self.latence)
        # type firrt name
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys(self.firstName)
        time.sleep(self.latence)
        # type employee id
        driver.find_element_by_id("employeeId").clear()
        driver.find_element_by_id("employeeId").send_keys(self.employeeId)
        time.sleep(self.latence)
        # save employee
        driver.find_element_by_id("btnSave").click()
        time.sleep(self.latence)
        driver.get_screenshot_as_file('C:\\Formation\\tmp\\add_employee.png')
        # check that Personal Detail page is present
        try:
            self.assertEqual("Personal Details",
                             driver.find_element_by_xpath("//div[@id='pdMainContainer']/div/h1").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        # check full name in Personal Detail page
        try:
            self.assertEqual(self.lastName + " " + self.firstName, driver.find_element_by_xpath("//div[@id='profile-pic']/h1").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        # edit details
        driver.find_element_by_id("btnSave").click()
        time.sleep(self.latence)
        # Gender : male
        driver.find_element_by_id("personal_optGender_1").click()
        time.sleep(self.latence)
        # Nation: French
        Select(driver.find_element_by_id("personal_cmbNation")).select_by_visible_text("French")
        time.sleep(self.latence)
        # Marital status : Single
        Select(driver.find_element_by_id("personal_cmbMarital")).select_by_visible_text("Single")
        time.sleep(self.latence)
        # Type date of birth
        driver.find_element_by_id("personal_DOB").clear()
        driver.find_element_by_id("personal_DOB").send_keys("2000-01-19")
        time.sleep(self.latence)
        # Save employee details
        driver.find_element_by_id("btnSave").click()
        time.sleep(self.latence)
        driver.get_screenshot_as_file('C:\\Formation\\tmp\\employee_details.png')


    def test_d_search_employee(self):
        # Search employee bi id
        driver = self.driver
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        time.sleep(self.latence)
        driver.find_element_by_id("menu_pim_viewEmployeeList").click()
        time.sleep(self.latence)
        # check that employee id field is present
        try:
            self.assertTrue(self.is_element_present(By.ID, "search-results"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        # type employee id
        driver.find_element_by_id("empsearch_id").clear()
        driver.find_element_by_id("empsearch_id").send_keys(self.employeeId)
        time.sleep(self.latence)
        # search
        driver.find_element_by_id("searchBtn").click()
        time.sleep(self.latence)
        driver.get_screenshot_as_file('C:\\Formation\\tmp\\search_employee.png')

    def test_e_delete_employee(self):
        driver = self.driver
        # Count rows in employee search result
        rows = len(driver.find_elements_by_xpath("//table[@id='resultTable']/tbody/tr"))
        # if only one employee, delete employee. This check is to prevent massive deletion
        if (rows==1):
            # click on all employee check box
            driver.find_element_by_xpath("//table[@id='resultTable']/tbody/tr/td/input").click()
            time.sleep(self.latence)
            # click on delete
            driver.find_element_by_id("btnDelete").click()
            time.sleep(self.latence)
            # confirm deletion
            driver.find_element_by_id("dialogDeleteBtn").click()
            time.sleep(self.latence)
            # check that employee list is empty
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Supervisor'])[1]/following::td[1]").click()
            time.sleep(self.latence)
            driver.get_screenshot_as_file('C:\\Formation\\tmp\\delete_employee.png')
        else:
            print ("More than one employee found. Cannot delete.")

    def test_z_logout(self):
        driver = self.driver
        # click on welcome
        driver.find_element_by_id("welcome").click()
        time.sleep(self.latence)
        # click on logout
        driver.find_element_by_xpath("//a[contains(@href, 'auth/logout')]").click()
        time.sleep(self.latence)
        driver.get_screenshot_as_file('C:\\Formation\\tmp\\logout.png')
        # verify that username is present
        try:
            self.assertTrue(self.is_element_present(By.ID, "txtUsername"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    # this method is run after all tests
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print(cls.verificationErrors)

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
