from behave import when, then
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

# The given step is now in common_steps.py

@when('I search for "Laptops"')
def step_impl(context):
    context.home_page.search_product("Laptops")
    context.search_results_page = SearchResultsPage(context.driver)

@when('I filter the results by brand, price range, CPU, processor count, OS, and item condition')
def step_impl(context):
    context.search_results_page.filter_laptops()

@then('I should write the product names to an Excel file')
def step_impl(context):
    context.search_results_page.write_product_names_to_excel('filtered_products.xlsx')
    context.driver.quit()
