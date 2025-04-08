from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('launch chrome browser')
def launchBrowser(context):
    context.browser = webdriver.Chrome()

@when('open orange hrm homepage')
def openHomePage(context):
    context.browser.get("https://opensource-demo.orangehrmlive.com/")

@then('verify that the logo is present on page')
def verifyLogo(context):
    logo = WebDriverWait(context.browser, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[1]'))
    )
    assert logo.is_displayed()

@then('close the browser')
def closeBrowser(context):
    context.browser.quit()
