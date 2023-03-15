import logging

from selenium.webdriver.common.by import By

from Locators.pageLocators import CompletedCheckoutLocators


class CompletedCheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.completed_text = ""

    def get_completed_order_text(self):
        self.completed_text = self.driver.find_element(By.XPATH, CompletedCheckoutLocators.complete_text_xpath).text

