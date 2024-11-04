import pytest

from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_login_page()


    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.should_be_login_link()
        main_page.go_to_login_page()

        login_page = LoginPage(browser, link)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        product_page = ProductPage(browser, link)
        basket_page = BasketPage(browser, link)
        product_page.open()
        # time.sleep(5)
        product_page.go_to_basket_page()
        basket_page.should_be_no_books_in_basket()
        basket_page.should_be_empty_basket_message()