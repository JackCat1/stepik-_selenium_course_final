from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    pass


class LoginPageLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, "form#register_form")
    AUTH_FORM = (By.CSS_SELECTOR, "form#login_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "form#add_to_basket_form .btn-add-to-basket")
    SUCCESS_ADD_BASKET_MESSAGE = (By.XPATH, "//div[contains(@class, 'alertinner')]")
    SUCCESS_ADD_BASKET_MESSAGE_PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'alertinner')]/strong")
    PRICE_BASKET_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-info')]/div[contains(@class, 'alertinner')]/p")
    PRICE_BASKET_MESSAGE_PRICE_VALUE = (By.XPATH, "//div[contains(@class, 'alert-info')]/div/p/strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
