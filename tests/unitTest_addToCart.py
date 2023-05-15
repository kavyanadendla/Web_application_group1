import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "kavya"
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
            # locate the "el-wrapper" div element
            el_wrapper = driver.find_element(By.XPATH, "//div[@class='el-wrapper']")

            # hover over the "el-wrapper" element
            hover = ActionChains(driver).move_to_element(el_wrapper)
            hover.perform()
            time.sleep(4)
            # Click on the "Add To Cart" button
            add_to_cart_link = self.driver.find_element(By.CLASS_NAME, "cart")
            expected_href = "http://127.0.0.1:8000/add-to-cart/1"
            self.assertEqual(add_to_cart_link.get_attribute("href"), expected_href)
            add_to_cart_link.click()

            time.sleep(2)

            # check cart count
            cart_count = self.driver.find_element(By.CLASS_NAME, "item-number").text
            self.assertEqual(cart_count, "1")



        except NoSuchElementException:
            driver.close()
            self.fail("Login Failed - user may not exist")

        time.sleep(3)


if __name__ == "__main__":
    unittest.main(warnings='ignore')
