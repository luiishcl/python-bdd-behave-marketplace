from behave import *
import requests

@given('the mock url')

def step_impl(context):

   context.url = "https://jsonplaceholder.typicode.com/todos/1"


@when('we consume the endpoint')

def step_impl(context):

   context.response = requests.session().get(context.url)


@then('json response is retrieved with right data and 200 as status code')

def step_impl(context):

   assert context.response.status_code == 200, "Response code is different: %s" % context.response.status_code + \
        " Error:" + str(context.response.content)

   json_response = context.response.json()

   assert json_response['id'] == 1, "Data is not the expected one: %s" % json_response