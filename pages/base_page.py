# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver

#     def wait_for_element(self, by_locator):
#         WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by_locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
