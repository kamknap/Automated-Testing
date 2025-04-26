from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@Given('The user see a list of products')
def step_login(context):
    pass

@When('The user adds a product to the shopping cart')
def step_add_to_cart(context):
    element_item = context.browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    element_item_name = context.browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    context.item_name = element_item_name.text 
    element_item.click()

@Then('The product appears in the shopping cart')
def step_verify_cart(context):
    element_cart_icon = context.browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    element_cart_icon.click()

    element_cart_item_name = context.browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')

    assert element_cart_item_name.text == context.item_name, "Zly produkt w koszyku"

@given('The user has a product added to the shopping cart')
def step_add_to_cart(context):
    element_item = context.browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    element_item.click()

@when('The user removes a product from the cart')
def remove_item_from_cart(context):
    element_cart_icon = context.browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    element_cart_icon.click()

    context.element_cart_item_name = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="item_4_title_link"]/div'))
    )

    element_cart_remove_btn = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-backpack"]'))
    )
    element_cart_remove_btn.click()


@then('The products disappears from the shopping cart')
def verify_remove_item(context):
    WebDriverWait(context.browser, 10).until(
        EC.invisibility_of_element_located((By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]'))
    )
    cart_contents = context.browser.find_elements(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]')
    assert len(cart_contents) == 0, 'Produkt dalej w koszyku'



