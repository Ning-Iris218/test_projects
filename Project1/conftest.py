import pytest
from selenium import webdriver
from login_page import LoginPage

@pytest.fixture(scope='module')
def login_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")

    login_sec=LoginPage(driver)
    login_sec.login('standard_user','secret_sauce')
    yield driver

    print('测试完成，准备关闭')
    driver.quit()