from multiprocessing import context

import requests
from behave import *


@Given(u'I have request the GET Api link and validate GET status code')
def step_impl6(context):
    responce = requests.get("http://localhost:3000/Database")
    assert responce.status_code == 200


@Given(u'I have request the GET Api link and validate POST status code')
def step_impl6(context):
    playload = {
        "postId": 1,
        "id": 500,
        "name": "id labore ex et quam laborum",
        "email": "Eliseo@gardner.biz",
        "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
    }
    responce = requests.post("http://localhost:3000/Database", json=playload)
    assert responce.status_code == 201


@Given(u'I have request the GET Api link and validate Delete status code')
def step_impl6(context):
    responce = requests.delete("http://localhost:3000/Database/500")
    assert responce.status_code == 200


@Given(u'I have request the GET Api link and validate PUT status code')
def step_impl6(context):
    playload = {
        "postId": 1,
        "id": 500,
        "name": "id labore ex et quam laborum",
        "email": "Eliseo@gardner.biz",
        "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
    }
    responce = requests.put("http://localhost:3000/Database/500", json=playload)
    assert responce.status_code == 200
