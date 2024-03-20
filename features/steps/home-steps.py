from behave import *
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from json import loads

BEES_URL_LOGIN = 'https://test-bees.herokuapp.com/users/sign_in'

@given(u'the TestBees home page is displayed')
def step_impl(context):
     context.browser.get(BEES_URL_LOGIN)


@when(u'do login')
def step_impl(context):
    text_from_access = loads(context.text)

    context.browser.find_element(By.ID, 'user_email').send_keys(text_from_access['email'])

    context.browser.find_element(By.ID, 'user_password').send_keys(text_from_access['password'])

    context.browser.find_element(By.CLASS_NAME, 'btn-primary').click()
    

@then(u'should present the homepage "Welcome to your storage"')
def step_impl(context):
    pass