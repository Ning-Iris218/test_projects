import pytest
from home_page import HomePage
from cart_page import Cart_Page
from information import Information_Page
from checkout_overview import  Checkout_Overview

def test_check_out(login_browser):
    driver=login_browser

    home_sec=HomePage(driver)
    cart_sec=Cart_Page(driver)
    info_sec=Information_Page(driver)
    checkout_sec=Checkout_Overview(driver)

    home_sec.add_all()
    home_sec.go_to_cart()
    cart_sec.checkout()

    info_sec.fill_info('Mary','Li','123456')
    info_sec.click_continue()
    checkout_sec.click_finish()
    complete_text=checkout_sec.get_complete()

    assert complete_text == 'Checkout: Complete!'

