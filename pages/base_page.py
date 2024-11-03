from selenium.common import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        # ваша реализация
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # def is_not_element_present(self, how, what, timeout=4):
    #     try:
    #         self.browser.implicitly_wait(timeout)
    #         self.browser.find_element(how, what)
    #     except NoSuchElementException:
    #         return True
    #     return False
    #
    # def is_disappeared(self, how, what, timeout=4):
    #     try:
    #         self.browser.implicitly_wait(timeout)
    #         self.browser.find_element(how, what)
    #     except NoSuchElementException:
    #         return True
    #     return False
    #
    # def should_be_authorized_user(self):
    #     assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
    #                                                                  " probably unauthorised user"
    #
    # def should_be_login_link(self):
    #     assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
    #
    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
    #     login_link.click()
    #
    # def should_be_authorized_user(self):
    #     assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
    #                                                                  " probably unauthorised user"
    #
    # def go_to_basket_page(self):
    #     basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
    #     basket_link.click()