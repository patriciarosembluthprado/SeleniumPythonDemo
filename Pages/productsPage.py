from selenium.webdriver.common.by import By

from Locators.pageLocators import ProductsPageLocators


class ProductsPage:
    def __init__(self, driver):
        self.products_list = None
        self.driver = driver

    def select_products(self):
        self.products_list = [self.driver.find_element(By.ID, ProductsPageLocators.back_pack_product_id),
                              self.driver.find_element(By.ID, ProductsPageLocators.bike_light_product_id),
                              self.driver.find_element(By.ID, ProductsPageLocators.bolt_t_shirt_product_id)]

    def add_products_to_cart(self):
        self.select_products()
        for product in self.products_list:
            product.click()

    def click_shopping_cart_icon(self):
        self.driver.find_element(By.ID, ProductsPageLocators.shopping_cart_icon_id).click()


