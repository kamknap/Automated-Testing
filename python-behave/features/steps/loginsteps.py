from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given('Lanuch chrome')
def launchChrome(context):
    context.browser=webdriver.Chrome()

@when(u'Open OrangeHRM homepage')
def step_impl(context):
    context.browser.get("https://opensource-demo.orangehrmlive.com/")

@when(u'Enter username "{usermane}" and password "{password}"')
def step_impl(context, username, password):
    time.sleep(2)
    username_field = context.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
    password_field = context.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
    username_field.send_keys(username)
    password_field.send_keys(password)

@when(u'Click the Login button')
def step_impl(context):
    button = context.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
    button.click()

@then(u'User succefully login to dashboard page')
def step_impl(context):
    time.sleep(2)
    text = context.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6')
    assert text.text == "Dashboard"
    context.browser.quit()