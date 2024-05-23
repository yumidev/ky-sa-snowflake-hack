from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FFService
from selenium.common.exceptions import WebDriverException

def get_selenium_driver():
    options = Options()
    options.add_argument("--headless")
    service = FFService(executable_path="/snap/bin/geckodriver")
    try:
        driver = webdriver.Firefox(options=options, service=service)
        return driver
    except WebDriverException as e:
        print(f"Selenium failed to create driver. Exception: {e}")
        return None
