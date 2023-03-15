from selenium.webdriver.common.by import By

from Locators.pageLocators import CheckoutOverviewLocators


class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def click_finish_button(self):
        self.driver.find_element(By.ID, CheckoutOverviewLocators.finish_button_id).click()
