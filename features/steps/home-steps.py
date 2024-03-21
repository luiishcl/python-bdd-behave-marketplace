from behave import *
from behave import given, when, then
from selenium.webdriver.common.by import By
from json import loads
import time

BEES_URL_LOGIN = 'https://test-bees.herokuapp.com/'

@given(u'the TestBees home page is displayed')
def step_impl(context):
     context.browser.get(BEES_URL_LOGIN)


@when(u'do login')
def step_impl(context):
    text_from_access = loads(context.text)

    context.browser.find_element(By.ID, 'user_email').send_keys(text_from_access['email'])

    context.browser.find_element(By.ID, 'user_password').send_keys(text_from_access['password'])
    
    context.browser.find_element(By.NAME, 'commit').click()

    time.sleep(5)
    

@then(u'should present "{welcome_text}"')
def step_impl(context, welcome_text):
    assert 'Welcome to your storage ' in context.browser.find_element(By.CLASS_NAME, 'h1').text