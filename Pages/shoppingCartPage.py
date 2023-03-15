from selenium.webdriver.common.by import By

from Locators.pageLocators import ShoppingCartLocators


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_checkout_button(self):
        self.driver.find_element(By.ID, ShoppingCartLocators.checkout_button_id).click()
