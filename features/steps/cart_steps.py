from behave import when, then
from pages.home_page import HomePage
from pages.cart_page import CartPage

# The given step is now in common_steps.py

@when('I search for "Nokia c22" and add it to the cart')
def step_impl(context):
    context.home_page.search_product("Nokia c22")
    context.home_page.add_product_to_cart_by_price("7999")

@when('I search for "keyboard wireless" and add "Dell USB Wireless Keyboard" to the cart')
def step_impl(context):
    context.home_page.search_product("keyboard wireless")
    context.home_page.add_product_to_cart_by_name("Dell USB Wireless Keyboard", quantity=2)

@then('I should validate the cart and proceed to checkout')
def step_impl(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.validate_cart()
    context.cart_page.proceed_to_checkout()
    context.driver.quit()
