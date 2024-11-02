from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):
    # def __init__(self, browser, url):
    #     super().__init__(browser, url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR,
                                       "#login_link"), "Login link is not presented"