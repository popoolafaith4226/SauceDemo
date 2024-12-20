import time

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from loginLocators.locator import Login_locators, Add_to_cart_locators, Click_add_cart_button, Click_checkout_button


class login_pages:
    def __init__(self,driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self, user_name):
        username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_locators.USERNAME))
        username.send_keys(user_name)

    def enter_password(self, pass_word):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_locators.PASSWORD))
        enter_password.send_keys(pass_word)

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_locators.LOGIN_BUTTON))
        login_button.click()

class add_to_cart:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart_button(self):
        click_add_to_cart = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Add_to_cart_locators.ADD_TO_CART))
        click_add_to_cart.click()
        time.sleep(3)


class cart_button:
    def __init__(self, driver):
        self.driver = driver

    def click_cart_button(self):
        click_the_cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_add_cart_button.CLICK_CART_BUTTON))
        click_the_cart_button.click()
        time.sleep(3)

class checkout_button:
    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        click_the_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_checkout_button.CHECKOUT_BUTTON))
        click_the_checkout_button.click()
