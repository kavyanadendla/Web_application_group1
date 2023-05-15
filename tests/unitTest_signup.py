import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import os

class TestCustomerSignUpForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_customer_signup_form(self):
        # Navigate to the web page containing the form
        self.driver.get("http://127.0.0.1:8000/customersignup")

        # Find the form elements by their IDs
        first_name_input = self.driver.find_element(By.ID, "id_first_name")
        last_name_input = self.driver.find_element(By.ID, "id_last_name")
        username_input = self.driver.find_element(By.ID, "id_username")
        password_input = self.driver.find_element(By.ID, "id_password")
        address_input = self.driver.find_element(By.ID, "id_address")
        mobile_input = self.driver.find_element(By.ID, "id_mobile")
        profile_pic_input = self.driver.find_element(By.ID, "id_profile_pic")
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")

        # Fill in the form fields
        first_name_input.send_keys("John")
        last_name_input.send_keys("Doe")
        username_input.send_keys("johndoe")
        password_input.send_keys("password123")
        address_input.send_keys("123 Main St.")
        mobile_input.send_keys("555-555-5555")
        time.sleep(2)
        # Get the path to the profile picture file
        profile_pic_path = r"D:\ChunnuWebDev\new\WebPharma\tests\testpic.jpg"

        # Upload the profile picture
        self.driver.execute_script('arguments[0].style.display="block";', profile_pic_input)
        self.driver.execute_script('arguments[0].value="";', profile_pic_input)
        profile_pic_input.send_keys(profile_pic_path)

        time.sleep(4)
        # Submit the form
        submit_button.click()

        time.sleep(3)
        # Verify that the user has been redirected to the login page
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/customerlogin")

if __name__ == '__main__':
    unittest.main()

