from behave import *
from os import *
import requests
import json
from resources.helper.api_utility import ApiUtility


apiUtility = ApiUtility()


@when('I send {string} request to endpoint {string}')
def send_request(context, method: str, endpoint: str) -> None:
    global response
    response = apiUtility.method_call(method, endpoint)

@then('The status code should be {string}')
def verify_status_code(context, status_code) -> None:
    actual_status_code = response.status_code
    assert actual_status_code == int(status_code)

@then('The POST response body should contain correct information')
def verify_response(context) -> None:
    pass
