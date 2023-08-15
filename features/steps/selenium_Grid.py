from behave.configuration import options
from selenium import webdriver


def step_impl1():
    val = input("enter which browser do you want run if edge type edge if chrome type chrome")
    if val == "edge":
        chrome_options1 = webdriver.ChromeOptions()
        chrome_options1.set_capability("browserName", "MicrosoftEdge")
        chrome_options1.set_capability("platformName", "Windows 11")
        chrome_options1.set_capability("ms:edgeOptions", {"args": ["--remote-allow-origins=*"]})
        driver = webdriver.Remote(
            command_executor='http://192.168.0.100:4444',
            options=chrome_options1)
        return driver

    elif val == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("browserName", "chrome")
        chrome_options.set_capability("platformName", "Windows 11")
        chrome_options.set_capability("goog:chromeOptions", {"args": ["--remote-allow-origins=*"]})
        driver = webdriver.Remote(
            command_executor='http://192.168.0.100:4444',
            options=chrome_options)
        return driver
