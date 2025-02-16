import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.Config import Config

from ActionPages.action_page import login_pages, add_to_cart, cart_button, checkout_button, first_name, last_name, \
    zip_code, continue_button, finish_button


@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()



@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = login_pages(driver)
    login_page.login_url(Config.BASEURL)
    return login_page


def tests_sauce_demo_login_page(login):
    login.enter_username(Config.USERNAME)
    login.enter_password(Config.PASSWORD)
    login.click_login_button()

def test_add_item_to_cart(login):
    add_item_to_cart = add_to_cart(login.driver)
    add_item_to_cart.add_to_cart_button()


def test_click_cart_button(login):
    click_cart_button = cart_button(login.driver)   #class
    click_cart_button.click_cart_button()

def test_checkout_button(login):
    click_checkout = checkout_button(login.driver)
    click_checkout.click_checkout()
#
# def test_first_name(login):
#    login.input_first_name(Config.FIRSTNAME) #first name


def test_first_name(login):
    input_first_name = first_name(login.driver)
    input_first_name.input_first_name(Config.FIRSTNAME)

def test_last_name(login):
    input_last_name = last_name(login.driver)
    input_last_name.input_last_name(Config.LASTNAME) #lastname

def test_zip_code(login):
    input_zip_code = zip_code(login.driver)
    input_zip_code.input_zip_code(Config.ZIPCODE) #zipcode

def test_continue_button(login):
    the_continue_button = continue_button(login.driver)
    the_continue_button.click_continue_button()

def test_finsh_button(login):
    the_finsh_button = finish_button(login.driver)
    the_finsh_button.click_finish_button() #clickthefinishproject