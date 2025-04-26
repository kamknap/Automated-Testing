from selenium import webdriver
from selenium.webdriver.common.by import By

def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.get('https://www.saucedemo.com/')
    username_input = context.browser.find_element(By.ID, 'user-name')
    password_input = context.browser.find_element(By.ID, 'password')
    login_button = context.browser.find_element(By.ID, 'login-button')
    username_input.send_keys('standard_user')
    password_input.send_keys('secret_sauce')
    login_button.click()

def after_scenario(context, scenario):
    context.browser.quit()