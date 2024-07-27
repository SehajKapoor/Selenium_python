# from behave import when, then
# from pages.home_page import HomePage
# from pages.search_results_page import SearchResultsPage

# # The given step is now in common_steps.py

# @when('I search for "iPhone 15"')
# def step_impl(context):
#     context.home_page.search_product("iPhone 15")
#     context.search_results_page = SearchResultsPage(context.driver)

# @then('I should print the search results with 4+ ratings to a text file')
# def step_impl(context):
#     context.search_results_page.print_search_results_to_file('search_results.txt')
#     context.driver.quit()

from behave import when, then, given
from selenium import webdriver
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

# # @given('I open the Amazon homepage')
# def step_impl(context):
#     context.driver = webdriver.Chrome()
#     context.driver.get("https://www.amazon.in/")
#     context.home_page = HomePage(context.driver)

@when('I search for "iPhone 15"')
def step_impl(context):
    context.home_page.search_product("iPhone 15")
    context.search_results_page = SearchResultsPage(context.driver)

@then('I should print the search results with 4+ ratings to a text file')
def step_impl(context):
    context.search_results_page.print_search_results_to_file('search_results.txt')
    context.driver.quit()
