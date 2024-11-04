import math
from selenium.common import NoAlertPresentException
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_ADD_BUTTON)
        button.click()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented"

    def should_be_product_name_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET)
        assert product_name.text == product_in_basket.text, \
            "Product name in not the same as in basket"

    def should_be_product_price_in_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert product_price.text == basket_price.text, \
            f"Basket price ({basket_price}) is not equal to product price ({product_price})"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
