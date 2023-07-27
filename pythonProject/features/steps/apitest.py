from multiprocessing import context

import requests
from behave import *
from behave.formatter import json


@Given(u'I have request the GET Api link "{url}" and validate status code "{code}"')
def step_impl6(context, url, code):
    responce = requests.get(url)
    status_code = responce.status_code
    print(status_code)
    print(code)
    assert status_code == code


@Given(u'I have request the POST Api link "{url}" and validate status code "{code1} and "{playload}"')
def step_impl6(context, url, code1, playload):
    responce = requests.post(url, json=playload)
    status_code_creat = responce.status_code
    print(status_code_creat)
    data = responce.json()
    print(data)
    assert status_code_creat != code1
