# from selenium.webdriver.common.by import By
# from .base_page import BasePage
# import openpyxl

# class SearchResultsPage(BasePage):
#     RESULTS = (By.XPATH, "//div[@data-component-type='s-search-result']")
#     PRODUCT_NAME = (By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']")
#     PRODUCT_RATING = (By.XPATH, ".//span[@class='a-icon-alt']")
#     DELIVERY_INFO = (By.XPATH, ".//span[@class='a-text-bold']")

#     def print_search_results_to_file(self, file_name):
#         results = self.driver.find_elements(*self.RESULTS)
#         with open(file_name, 'w') as file:
#             for result in results:
#                 rating = result.find_element(*self.PRODUCT_RATING).text
#                 if '4' in rating:
#                     delivery = result.find_element(*self.DELIVERY_INFO).text
#                     if 'next day' in delivery:
#                         file.write(result.text + '\n')

#     def filter_laptops(self):
#         # Implement filtering logic based on the criteria given in the assignment
#         pass

#     def write_product_names_to_excel(self, file_name):
#         wb = openpyxl.Workbook()
#         ws = wb.active
#         ws.append(['Product Name'])
#         products = self.driver.find_elements(*self.PRODUCT_NAME)
#         for product in products:
#             ws.append([product.text])
#         wb.save(file_name)

#     def print_catalogue_images_and_reviews(self, file_name):
#         images = self.driver.find_elements(By.CSS_SELECTOR, '.image')
#         reviews = self.driver.find_elements(By.XPATH, "//a[@class='a-size-base a-link-normal']")
#         with open(file_name, 'w') as file:
#             for img in images:
#                 file.write(img.get_attribute('src') + '\n')
#                 img.click()
#             for review in reviews:
#                 if '3 star' in review.text:
#                     file.write(review.text + '\n')
from selenium.webdriver.common.by import By
from .base_page import BasePage
import openpyxl

class SearchResultsPage(BasePage):
    RESULTS = (By.XPATH, "//div[@data-component-type='s-search-result']")
    PRODUCT_NAME = (By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']")
    PRODUCT_RATING = (By.XPATH, ".//span[@class='a-icon-alt']")
    DELIVERY_INFO = (By.XPATH, ".//span[@class='a-text-bold']")

    def print_search_results_to_file(self, file_name):
        self.wait_for_element(self.RESULTS)
        results = self.driver.find_elements(*self.RESULTS)
        print(f"Found {len(results)} results")  # Debugging statement
        with open(file_name, 'w') as file:
            for result in results:
                try:
                    rating = result.find_element(*self.PRODUCT_RATING).text
                    print(f"Rating found: {rating}")  # Debugging statement
                    if '4' in rating:
                        delivery = result.find_element(*self.DELIVERY_INFO).text
                        print(f"Delivery info: {delivery}")  # Debugging statement
                        if 'next day' in delivery:
                            file.write(result.text + '\n')
                except Exception as e:
                    print(f"Error processing result: {e}")  # Debugging statement

    def filter_laptops(self):
        # Implement filtering logic based on the criteria given in the assignment
        pass

    def write_product_names_to_excel(self, file_name):
        self.wait_for_element(self.RESULTS)
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(['Product Name'])
        products = self.driver.find_elements(*self.PRODUCT_NAME)
        print(f"Found {len(products)} products")  # Debugging statement
        for product in products:
            ws.append([product.text])
        wb.save(file_name)

    def print_catalogue_images_and_reviews(self, file_name):
        self.wait_for_element(self.RESULTS)
        images = self.driver.find_elements(By.CSS_SELECTOR, '.image')
        reviews = self.driver.find_elements(By.XPATH, "//a[@class='a-size-base a-link-normal']")
        with open(file_name, 'w') as file:
            for img in images:
                try:
                    file.write(img.get_attribute('src') + '\n')
                except Exception as e:
                    print(f"Error processing image: {e}")  # Debugging statement
            for review in reviews:
                try:
                    if '3 star' in review.text:
                        file.write(review.text + '\n')
                except Exception as e:
                    print(f"Error processing review: {e}")  # Debugging statement
