import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

def should_be_element(browser):
    try:
        browser.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    except NoSuchElementException:
        return False
    return True

def test_page_contains_adding_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    browser.get(link)
    time.sleep(30)
    element = should_be_element(browser)
    assert element, 'Element button to add book to basket was not found'



