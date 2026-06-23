import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='module')
def set_up_browser():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    print('Done')
    driver.quit()


@pytest.fixture(scope='module',params=['standard_user','performance_glitch_user','locked_out_user'])
def provider(request):
    current_user=request.param
    print(f"\n本轮传输{current_user}")
    yield current_user

@pytest.fixture(scope='module')
def login(set_up_browser,provider):
   driver=set_up_browser
   driver.get('https://www.saucedemo.com/')
   print(f'正在测试{provider}')
   driver.find_element(By.ID,'user-name').send_keys(provider)
   driver.find_element(By.ID,'password').send_keys("secret_sauce")
   driver.find_element(By.ID,'login-button').click()
   yield driver
   print(f'{provider} is Over')
   try:
       driver.find_element(By.ID,'react-burger-menu-btn').click()
       driver.find_element(By.ID,'logout_sidebar_link').click()
   except Exception as e:
        pass
   print('over')