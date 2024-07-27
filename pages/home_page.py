from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')

    def search_product(self, product_name):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(product_name)
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def add_product_to_cart_by_price(self, price):
        self.driver.find_element(By.XPATH, f"//span[contains(text(), '{price}')]").click()
        self.driver.find_element(By.ID, 'add-to-cart-button').click()

    def add_product_to_cart_by_name(self, product_name, quantity=1):
        self.driver.find_element(By.XPATH, f"//span[contains(text(), '{product_name}')]").click()
        self.driver.find_element(By.ID, 'add-to-cart-button').click()
        for _ in range(quantity - 1):
            self.driver.find_element(By.ID, 'add-to-cart-button').click()
