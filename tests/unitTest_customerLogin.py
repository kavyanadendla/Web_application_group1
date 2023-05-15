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
           elem = driver.find_element(By.LINK_TEXT, "Logout")
           driver.close()
           assert True

        except NoSuchElementException:
            driver.close()
            self.fail("Login Failed - user may not exist")

        time.sleep(3)


if __name__ == "__main__":
    unittest.main(warnings='ignore')
