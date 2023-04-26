from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_card_button(browser):

    browser.get(link)

    assert browser.find_elements(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket'), 'basket button not found'

    time.sleep(10)
