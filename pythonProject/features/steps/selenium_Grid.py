from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Remote(
   command_executor='https://{{ip or host}}:4444/wd/hub')

