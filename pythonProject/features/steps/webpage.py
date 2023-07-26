from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@given('I have launched the application')
def lanchbrowser(context):
    context.driver = webdriver.Edge("msedgedriver.exe")


@then('I should land on home page')
def getlink(context):
    context.driver.get("https://jsonplaceholder.typicode.com/")


@given('I have quit the application')
def quitbrowser(context):
    context.driver.close()