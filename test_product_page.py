import time
import faker
import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestAddToBasket:
    """Для девяти прогонов раскомментировать @pytest.mark.parametrize ниже"""
    # Для всех прогонов
    # @pytest.mark.parametrize('promo_offer', [
    #     f"offer{num}" for num in range(7)] +
    #                          [pytest.param('offer7', marks=pytest.mark.xfail
    #                              (reason="expected to fail to check negative scenario"))] +
    #                          [f"offer{num}" for num in range(8, 10)]
    #                          )
    """Для одного прогона раскомментировать @pytest.mark.parametrize('promo_offer', [f"offer1"])"""
    @pytest.mark.parametrize('promo_offer', [f"offer1"])
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        base_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        link = f"{base_url}/?promo={promo_offer}"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        # time.sleep(5)
        page.should_be_success_message()
        page.should_be_product_name_in_basket()
        page.should_be_product_price_in_basket()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link, 0)
        page.open()
        # time.sleep(5)
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="expected to fail to check negative scenario")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link, 0)
        page.open()
        page.add_to_basket()
        # time.sleep(5)
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="expected to fail to check negative scenario")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link, 0)
        page.open()
        page.add_to_basket()
        # time.sleep(5)
        page.should_be_disappeared_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.should_be_login_page()



    # For checking assertion error with negative scenario
    @pytest.mark.xfail(reason="Expected to fail. Checking negative scenario")
    def test_guest_cant_see_product_in_empty_basket_with_error(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        product_page = ProductPage(browser, link)
        basket_page = BasketPage(browser, link)
        product_page.open()
        # time.sleep(5)
        product_page.add_to_basket()
        product_page.go_to_basket_page()
        basket_page.should_be_no_books_in_basket()
        basket_page.should_be_empty_basket_message()

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        self.product_page = ProductPage(browser, link)
        login_page.open()
        f = faker.Faker()
        email = f.email(domain="example.com")
        password = f.password(length=10)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        basket_page = BasketPage(browser, link)
        product_page.open()
        # time.sleep(5)
        product_page.go_to_basket_page()
        basket_page.should_be_no_books_in_basket()
        basket_page.should_be_empty_basket_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.product_page = ProductPage(browser, link)
        self.product_page.open()
        self.product_page.add_to_basket()
        self.product_page.should_be_success_message()
        self.product_page.should_be_product_name_in_basket()
        self.product_page.should_be_product_price_in_basket()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.product_page = ProductPage(browser, link)
        self.product_page.open()
        # time.sleep(5)
        self.product_page.should_not_be_success_message()