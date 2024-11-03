import time

import pytest
from selenium.common.exceptions import NoAlertPresentException
import math
from pages.product_page import ProductPage

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
base_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

@pytest.mark.parametrize('promo_offer', [
    f"offer{num}" for num in range(7)] +
    [pytest.param('offer7', marks=pytest.mark.xfail(reason="bug"))] +
    [f"offer{num}" for num in range(8, 10)]
)
class TestAddToBasket():
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


