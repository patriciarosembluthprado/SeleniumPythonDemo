from selenium.webdriver.common.by import By

from Locators.pageLocators import ProductsPageLocators


class ProductsPage:
    def __init__(self, driver):
        self.products_list = None
        self.driver = driver

    def select_products(self, driver):
        self.products_list = [self.driver.find_element(By.ID, ProductsPageLocators.back_pack_product_id),
                              self.driver.find_element(By.ID, ProductsPageLocators.bike_light_product_id),
                              self.driver.find_element(By.ID, ProductsPageLocators.bolt_t_shirt_product_id)]

    def add_products_to_cart(self, driver):
        self.select_products(driver)
        for self.product in self.products_list:
            self.product.click()


