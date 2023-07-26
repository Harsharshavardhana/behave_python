from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given(u'I have launched the application')
def step_impl1(context):
    context.driver = webdriver.Edge()


@then(u'I should enter the swags lab page')
def step_impl2(context):
    context.driver.get("https://www.saucedemo.com/")


@Given(u'i should enter the username')
def step_impl3(context):
    username = context.driver.find_element(By.ID, "user-name")
    username.send_keys(Keys.ENTER)
    username.sendkey("standard_user")


@Given(u'i should enter the password')
def step_impl4(context):
    password = context.driver.find_element(By.ID, "password")
    password.send_keys(Keys.ENTER,"secret_sauce")
    password.sendkey("secret_sauce")


@then(u'click login button')
def step_impl4(context):
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()


@then(u'I should land on home page')
def step_impl4(context):
    verify_text = context.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[1]/div[2]/div').getText()
    assert verify_text == 'Example Domains'


@given(u'I have quit the application')
def step_impl3(context):
    context.driver.close()
