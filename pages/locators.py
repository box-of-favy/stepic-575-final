from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    BASKET_ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR,
                         "div#messages div.alert-success:first-child > .alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages > div.alert-success:first-child")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.row p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span > a[href*='basket']")

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "div#content_inner > p")
    BOOKS_IN_BASKET = (By.CSS_SELECTOR, "form h3")