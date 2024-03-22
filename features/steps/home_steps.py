from behave import given, when, then
from json import loads
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

BEES_URL_LOGIN = 'https://test-bees.herokuapp.com/'

@given('the "{page_name}" is displayed')
def go_to_page(context, page_name):
    context.browser.get(BEES_URL_LOGIN)
    title = context.browser.find_element(By.TAG_NAME, 'h2').text
    assert title in page_name
    

@when('do login')
def do_login(context):
    credentials = loads(context.text)
    
    email_imput = context.browser.find_element(By.ID, 'user_email')
    email_imput.send_keys(credentials['email'])

    pass_imput = context.browser.find_element(By.ID, 'user_password')
    pass_imput.send_keys(credentials['password'])
    
    click_submit_login = context.browser.find_element(By.CLASS_NAME, 'gap-2')
    click_submit_login.click()

    # element = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))


@then('should present "{welcome_text}"')
def step_impl(context, welcome_text):
     text_welcome_home = context.browser.find_element(By.TAG_NAME, 'h1').text
     assert text_welcome_home in welcome_text