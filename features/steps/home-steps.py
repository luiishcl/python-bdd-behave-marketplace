from behave import *
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

BEES_URL_LOGIN = 'https://test-bees.herokuapp.com/users/sign_in'

@given(u'the TestBees home page is displayed')
def step_impl(context):
     context.browser.get(BEES_URL_LOGIN)


@when(u'the user provide email "{email}"')
def step_impl(context, email):
    search_imput = context.browser.find_element(By.ID, 'user_email')
    search_imput.send_keys(email + Keys.RETURN)


@When(u'the user provide password "{password}"')
def step_impl(context, password):
    search_imput = context.browser.find_element(By.ID, 'user_password')
    search_imput.send_keys(password + Keys.RETURN)


@when(u'Click on Submit')
def step_impl(context):
    submitt_button = context.browser.find_element(By.CLASS_NAME, 'btn-primary')
    submitt_button.click()
    

@then(u'should present the homepage "Welcome to your storage"')
def step_impl(context):
    pass