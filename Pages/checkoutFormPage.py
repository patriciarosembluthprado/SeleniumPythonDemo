from selenium.webdriver.common.by import By

from Locators.pageLocators import CheckoutFormLocators


class CheckoutInfoPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, CheckoutFormLocators.first_name_field_id).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, CheckoutFormLocators.last_name_field_id).send_keys(last_name)

    def enter_zip_code(self, zip_code):
        self.driver.find_element(By.ID, CheckoutFormLocators.zip_code_field_id).send_keys(zip_code)

    def click_continue_button(self):
        self.driver.find_element(By.ID, CheckoutFormLocators.continue_button_id).click()
