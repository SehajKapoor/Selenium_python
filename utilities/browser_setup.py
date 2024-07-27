from selenium import webdriver

def setup_browser():
    driver = webdriver.Chrome()
    return driver
