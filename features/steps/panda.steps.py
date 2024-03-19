from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


DUCKDUCKGO_HOME = 'https://duckduckgo.com/'

@given(u'the DuckDuckGo home page is displayed')
def step_impl(context):
    context.web.get(DUCKDUCKGO_HOME)


@when(u'the user searches for "{phrase}"')
def step_impl(context, phrase):
    search_input = context.web.find_element(By.NAME,'q')
    search_input.send_keys(phrase + Keys.RETURN)


@then(u'results are shown for "{phrase}"')
def step_impl(context, phrase):
    links_div = context.web.find_element(By.ID,'react-layout')
    #assert len(links_div.find_element(By.XPATH,'//div')) > 0 TBD
    search_input = context.web.find_element(By.NAME,'q')
    assert search_input.get_attribute('value') == phrase