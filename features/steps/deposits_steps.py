from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from json import loads
# from urllib.parse import urlparse
from urllib.parse import urlparse, urljoin


DEPOSIT_URL = "https://test-bees.herokuapp.com/deposits"
SUCCESSFUL_MSG_DEFAULT = 'Deposit was successfully created.'
DEPOSIT_ID = "deposits/189"

@given('stay on "{deposit_page}" session')
def go_to_page(context, deposit_page):
    context.browser.get(DEPOSIT_URL)
    title = context.browser.find_element(By.TAG_NAME, 'h1').text
    assert title in deposit_page


@given('stay "{deposit_edit}" session')
def step_impl(context, deposit_edit):
    base_url_deposit = DEPOSIT_URL
    relative_path_deposit = DEPOSIT_ID
    final_url = urljoin(base_url_deposit, relative_path_deposit)
    print(final_url)  # Output: 
    context.browser.get(final_url)

    link_check_dp = context.browser.find_element(By.LINK_TEXT, 'Edit this deposit').text
    assert link_check_dp in deposit_edit
    

@when('create a new deposit')
def create_deposit(context):
    
    context.browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    create_new_deposit_link = context.browser.find_element(By.LINK_TEXT, 'New deposit')
    create_new_deposit_link.click()

    info_deposits = loads(context.text)
    deposit_imput_name = context.browser.find_element(By.ID, 'deposit_name')
    deposit_imput_name.send_keys(info_deposits['name'])

    deposit_imput_address = context.browser.find_element(By.ID, 'deposit_address')
    deposit_imput_address.send_keys(info_deposits['address'])

    deposit_imput_city = context.browser.find_element(By.ID, 'deposit_city')
    deposit_imput_city.send_keys(info_deposits['city'])

    deposit_imput_state = context.browser.find_element(By.ID, 'deposit_state')
    deposit_imput_state.send_keys(info_deposits['state'])

    deposit_imput_zipcode = context.browser.find_element(By.ID, 'deposit_zipcode')
    deposit_imput_zipcode.send_keys(info_deposits['zipcode'])

    create_deposit_button = context.browser.find_element(By.CLASS_NAME, 'btn-primary')
    create_deposit_button.click()


@then('the deposits were created successful')
def verify_deposit(context):
    
    successful_msg_deposit_created = context.browser.find_element(By.TAG_NAME, 'p').text
    assert successful_msg_deposit_created in SUCCESSFUL_MSG_DEFAULT
    print(successful_msg_deposit_created)

    # Capture path from actual URL to use on deposits manager
    url_parseada = urlparse(context.browser.current_url).path
    print(url_parseada)
    
    back_to_deposit_link = context.browser.find_element(By.LINK_TEXT, 'Back to deposits')
    back_to_deposit_link.click()


@when(u'edit a deposit')
def step_impl(context):
    ...



@then(u'the deposits were edited successful')
def step_impl(context):
    ...