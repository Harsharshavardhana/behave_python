from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_Grid import step_impl1


@Given(u'I have launched the application')
def step_impl10(context):
    context.driver = step_impl1()


@then(u'I should enter the swags lab page')
def step_impl2(context):
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()


@Given(u'i should enter the username as "{name}"')
def step_impl3(context, name):
    username = context.driver.find_element(By.ID, "user-name")
    username.send_keys(Keys.ENTER + name)


@Given(u'i should enter the password as "{ps_w}"')
def step_impl4(context, ps_w):
    password = context.driver.find_element(By.ID, "password")
    password.send_keys(Keys.ENTER + ps_w)


@then(u'click login button')
def step_impl5(context):
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()


@then(u'I should land on home page validate login successfully')
def step_impl6(context):
    verify_text = context.driver.find_element(By.XPATH, "//*[@id='header_container']/div[1]/div[2]/div")
    assert verify_text.text == "Swag Labs"


@then(u'I should land on home page validate login unsuccessfully "{verification}')
def step_impl7(context, verification):
    verify_text = context.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]")
    assert verify_text.text == verification


@given(u'I have quit the application')
def step_impl8(context):
    context.driver.close()
