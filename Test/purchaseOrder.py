import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Pages.loginPage import LoginPage
from Pages.productsPage import ProductsPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.options = Options()
        cls.options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                      options=cls.options)

    def test_purchase_order(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        login = LoginPage(driver)
        products = ProductsPage(driver)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()
        products.add_products_to_cart(driver)
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()