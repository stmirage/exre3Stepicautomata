import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
answer = lambda : math.log(int(time.time()))


def test_buy_buuton_is_active(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    button_class = "btn-add-to-basket"
    browser.get(link)
    time.sleep(30)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, button_class))
    )
    button = browser.find_element_by_css_selector(f'.{button_class}')
    assert button.text != ''
