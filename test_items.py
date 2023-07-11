import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
class TestMainPage1():
    def test_guest(self, browser):
        browser.get(link)
        submit_button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
        submit_button.click()
        time.sleep(2)