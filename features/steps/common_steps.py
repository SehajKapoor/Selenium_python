from behave import given
from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage

@given('I open the Amazon homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.amazon.in/")
    context.login_page = LoginPage(context.driver)
    context.home_page = HomePage(context.driver)
