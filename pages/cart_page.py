from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = (By.XPATH, "//div[@data-name='Active Items']")
    PROCEED_TO_CHECKOUT_BUTTON = (By.NAME, 'proceedToRetailCheckout')

    def validate_cart(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        for item in items:
            print(item.text)
        # Additional validation logic

    def proceed_to_checkout(self):
        self.driver.find_element(*self.PROCEED_TO_CHECKOUT_BUTTON).click()
