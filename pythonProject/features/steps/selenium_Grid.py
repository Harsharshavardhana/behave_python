from selenium import webdriver


def step_impl1():
    chrome_options = webdriver.EdgeOptions()
    chrome_options.set_capability("browserVersion", "69")
    chrome_options.set_capability("platformName", "Windows 10")
    driver = webdriver.Remote(
        command_executor='http://localhost:4444',
        options=chrome_options)
    #driver = webdriver.Edge()
    return driver
