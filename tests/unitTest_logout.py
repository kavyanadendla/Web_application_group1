import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "dhitika"
        pwd = "12345678"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/customerlogin")

        elem = driver.find_element(By.ID,"id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID,"id_password")
        elem.send_keys(pwd)
        time.sleep(5)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/customer-home")
        time.sleep(3)

        try:
            # attempt to find the 'Logout' button - if found, logged in
           logout_link = driver.find_element(By.LINK_TEXT, "Logout")
           logout_link.click()
           time.sleep(2)
           driver.get("http://127.0.0.1:8000/logout")
           logout_successful_elements = self.driver.find_elements(By.TAG_NAME, 'h2')

           found = False
           for element in logout_successful_elements:
            if "You've logged out successfully!" in element.text:
                found = True
                break

           self.assertTrue(found, "Logout message not found")

        except NoSuchElementException:
            driver.close()
            self.fail("Login Failed - user may not exist")

        time.sleep(3)


if __name__ == "__main__":
    unittest.main(warnings='ignore')
