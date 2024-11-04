import time

import pytest
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
import math

from pages.login_page import LoginPage
from pages.product_page import ProductPage

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
base_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


class TestAddToBasket():
    @pytest.mark.parametrize('promo_offer', [
        f"offer{num}" for num in range(7)] +
                             [pytest.param('offer7', marks=pytest.mark.xfail(reason="bug"))] +
                             [f"offer{num}" for num in range(8, 10)]
                             )
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        link = f"{base_url}/?promo={promo_offer}"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        time.sleep(5)
        page.should_be_success_message()
        page.should_be_product_name_in_basket()
        page.should_be_product_price_in_basket()

    @pytest.mark.xfail()
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link, 0)
        page.open()
        page.add_to_basket()
        # time.sleep(60)
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link, 0)
        page.open()
        # time.sleep(5)
        page.should_not_be_success_message()

    @pytest.mark.xfail()
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link, 0)
        page.open()
        page.add_to_basket()
        time.sleep(5)
        page.should_be_disappeared_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.should_be_login_page()