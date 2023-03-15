import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Pages.loginPage import LoginPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.options = Options()
        cls.options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                      options=cls.options)

    def test_valid_login(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        login = LoginPage(driver)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
