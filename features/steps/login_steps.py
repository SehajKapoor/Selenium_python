from behave import when, then
from pages.login_page import LoginPage
from pages.home_page import HomePage

# The given step is now in common_steps.py

@when('I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)

@then('I should see the homepage if credentials are "{validity}"')
def step_impl(context, validity):
    home_page = HomePage(context.driver)
    if validity == 'valid':
        assert home_page.is_home_page_displayed()
    else:
        assert context.login_page.is_login_error_displayed()
    context.driver.quit()
