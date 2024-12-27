from selenium.webdriver.common.by import By


class Login_locators:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

class Add_to_cart_locators:
    ADD_TO_CART = (By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button")

class Click_add_cart_button:
    CLICK_CART_BUTTON = (By.ID, "shopping_cart_container")

class Click_checkout_button:
    CHECKOUT_BUTTON = (By.XPATH, "//*[@id='cart_contents_container']/div/div[2]/a[2]")

class First_name:
    FIRSTNAME = (By.ID, "first-name")

class Last_name:
    LASTNAME = (By.ID, "last-name")

class Zip_code:
    ZIP_CODE = (By.ID, "postal-code")

class Click_continue_button:
    CONTINUE_BUTTON = (By.XPATH, "//*[@id='checkout_info_container']/div/form/div[2]/input")

class Click_finish_button:
    FINISH_BUTTON = (By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[8]/a[2]")
