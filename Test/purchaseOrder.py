import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from Helpers.dataGenerator import DataGenerator
from Pages.checkoutFormPage import CheckoutInfoPage
from Pages.checkoutOverviewPage import CheckoutOverviewPage
from Pages.completedCheckoutPage import CompletedCheckoutPage
from Pages.loginPage import LoginPage
from Pages.productsPage import ProductsPage
from Pages.shoppingCartPage import ShoppingCartPage


class PurchaseOrder(unittest.TestCase):

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
        shopping_cart = ShoppingCartPage(driver)
        checkout_form = CheckoutInfoPage(driver)
        checkout_overview = CheckoutOverviewPage(driver)
        completed_checkout = CompletedCheckoutPage(driver)
        data = DataGenerator()

        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()
        products.add_products_to_cart()
        products.click_shopping_cart_icon()
        shopping_cart.click_checkout_button()
        checkout_form.enter_first_name(data.first_name())
        checkout_form.enter_last_name(data.last_name())
        checkout_form.enter_zip_code(data.zip_code())
        checkout_form.click_continue_button()
        checkout_overview.click_finish_button()
        completed_checkout.get_completed_order_text()
        actual_text = completed_checkout.completed_text
        self.assertEqual("Your order has been dispatched, and will arrive just as fast as the pony can get there!",
                         actual_text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()



