from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, 'ap_email')
    CONTINUE_BUTTON = (By.ID, 'continue')
    PASSWORD_INPUT = (By.ID, 'ap_password')
    SIGNIN_BUTTON = (By.ID, 'signInSubmit')
    LOGIN_ERROR = (By.XPATH, "//span[@class='a-list-item']")

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.SIGNIN_BUTTON).click()

    def is_login_error_displayed(self):
        return self.driver.find_element(*self.LOGIN_ERROR).is_displayed()
