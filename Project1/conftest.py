import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from login_page import LoginPage

@pytest.fixture(scope='module')
def login_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")

    login_sec=LoginPage(driver)
    login_sec.login('standard_user','secret_sauce')
    yield driver

    print('测试完成，准备关闭')
    driver.quit()