from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given('launch browser')
def launchBrowser(context):
    context.browser = webdriver.Chrome()

@when('contact form page opens')
def openWebsite(context):
    context.browser.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")


@when('enter username "user", password "pass123", text in textarea "test text 123", click Checkbox1 and Checkbox2, unclick Checkbox3')
def enterData(context):
    username_field = context.browser.find_element(By.XPATH, '//*[@id="HTMLFormElements"]/table/tbody/tr[1]/td/input')
    password_field = context.browser.find_element(By.XPATH, '//*[@id="HTMLFormElements"]/table/tbody/tr[2]/td/input')
    texarea_field = context.browser.find_element(By.XPATH, '//*[@id="HTMLFormElements"]/table/tbody/tr[3]/td/textarea')
    checkbox1 = context.browser.find_element(By.XPATH, '//*[@id="HTMLFormElements"]/table/tbody/tr[5]/td/input[1]')
    checkbox2 = context.browser.find_element(By.XPATH, '//*[@id="HTMLFormElements"]/table/tbody/tr[5]/td/input[2]')
    checkbox3 = context.browser.find_element(By.XPATH, '//*[@id="HTMLFormElements"]/table/tbody/tr[5]/td/input[3]')
    username_field.send_keys("user")
    password_field.send_keys("pass123")
    texarea_field.send_keys("test text 123")
    if not checkbox1.is_selected():
        checkbox1.click()
    if not checkbox2.is_selected():
        checkbox2.click()
    if checkbox3.is_selected():
        checkbox3.click()


@when('click the "Submit" button')
def clickSubmit(context):
    btn = context.browser.find_element(By.XPATH, '//*[@id="HTMLFormElements"]/table/tbody/tr[9]/td/input[2]')
    btn.click()


@then('user is directed to new page and displayed information equals written by user')
def verifyData(context):
    username_data = context.browser.find_element(By.XPATH, '//*[@id="_valueusername"]')
    password_data = context.browser.find_element(By.XPATH, '//*[@id="_valuepassword"]')
    textarea_data = context.browser.find_element(By.XPATH, '//*[@id="_valuecomments"]')
    assert username_data.text == "user"
    assert password_data.text == "pass123"
    assert textarea_data.text == "test text 123"
    context.browser.quit()