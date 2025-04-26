from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Launch browser chrome')
def step_launch_browser(context):
    context.browser = webdriver.Chrome()

@when('Login form appears')
def step_open_website(context):
    context.browser.get("https://www.saucedemo.com/")

@when('Enter username "standard_user", password "secret_sauce"')
def step_insert_values(context):
    username_input = context.browser.find_element(By.ID, "user-name")
    password_input = context.browser.find_element(By.ID, "password")
    username_input.send_keys('standard_user')
    password_input.send_keys('secret_sauce')

@when('Click Login button')
def step_click_login_button(context):
    login_button = context.browser.find_element(By.ID, "login-button")
    login_button.click()

@then('User is being logged in and products list appears')
def step_check_product_list(context):
    product_element = context.browser.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]')
    assert product_element.is_displayed(), "Produkt nie jest widoczny!"
    context.browser.quit()
