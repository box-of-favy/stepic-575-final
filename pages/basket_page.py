import pytest

from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_no_books_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BOOKS_IN_BASKET), \
            "Basket has books but should be empty"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Basket has no message that it is empty"