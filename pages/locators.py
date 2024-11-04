from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span a[href*='basket']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert-success:first-child > .alertinner")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages div.alert-success:first-child > .alertinner")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")
    EMPTY_BASKET = (By.CSS_SELECTOR, "div#content_inner > p > a")
    BOOKS_IN_BASKET = (By.CSS_SELECTOR, "form h3")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")