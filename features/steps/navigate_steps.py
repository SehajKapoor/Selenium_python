from behave import when, then
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

# The given step is now in common_steps.py

@when('I search for "Nokia c22"')
def step_impl(context):
    context.home_page.search_product("Nokia c22")
    context.search_results_page = SearchResultsPage(context.driver)

@then('I should print product catalogue images and 3-star reviews to a text file')
def step_impl(context):
    context.search_results_page.print_catalogue_images_and_reviews('product_catalogue_reviews.txt')
    context.driver.quit()
