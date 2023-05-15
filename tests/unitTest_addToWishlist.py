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
        user = "deepika"
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
            # Click on the "Add To Wishlist" button
            add_to_cart_link = self.driver.find_element(By.CSS_SELECTOR, 'a.cart[href="/wishlist/add/1/"]')
            add_to_cart_link.click()

            time.sleep(2)

            # check whishlist count
            driver.get("http://127.0.0.1:8000/wishlist")
            time.sleep(2)
            # Check the number of products in the wishlist
            wishlist_count = None
            wishlist_count_elements = self.driver.find_elements(By.TAG_NAME, 'p')
            for element in wishlist_count_elements:
                if 'wishlist' in element.text:
                    wishlist_count = element.text
                    break

            if wishlist_count is not None:
                # Get the actual wishlist count
                actual_count = wishlist_count.replace('Number of products in wishlist:', "").strip()

                # Check if the actual wishlist count matches the expected count
                self.assertEqual(actual_count, "1")
            else:
                self.fail("Could not find wishlist count element")


        except NoSuchElementException:
            driver.close()
            self.fail("Login Failed - user may not exist")

        time.sleep(3)


if __name__ == "__main__":
    unittest.main(warnings='ignore')
