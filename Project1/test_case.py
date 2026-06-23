import pytest
from home_page import HomePage
from cart_page import Cart_Page

def test_remove_backpack(login_browser):
    driver=login_browser

    home_sec=HomePage(driver)
    cart_sec=Cart_Page(driver)

    home_sec.add_backpack()

    home_sec.go_to_cart()
    cart_sec.remove_backpack()
    count_in_cart=cart_sec.get_items_count()

    assert count_in_cart == 0



