from logging import exception
from selenium.webdriver.common.by import By

def test_login2(login):
   driver=login
   print('正在测试能否正常展示')
   assert driver.find_element(By.CLASS_NAME,'shopping_cart_link').is_displayed()



# @pytest.fixture(scope='module')
# def login(set_up_browser):
#     driver=set_up_browser
#     driver.get('https://www.saucedemo.com/')
#     driver.find_element(By.ID,'user-name').send_keys("standard_user")
#     driver.find_element(By.ID,'password').send_keys("secret_sauce")
#     driver.find_element(By.ID,'login-button').click()
#     yield driver
#     print('Over')
#
# def test_check(login):
#     driver=login
#     driver.find_element(By.CLASS_NAME, "inventory_item_name").click()
#     WebDriverWait(driver,10).until(
#         EC.presence_of_element_located((By.CLASS_NAME,"inventory_details_name"))
#     )
#     driver_title=driver.find_element(By.CLASS_NAME,"inventory_details_name").text
#     print(driver_title)
#     assert "Backpack" in driver_title
#     print("Pass")

# def test_case1(set_up_browser):
#     print('Start case1')
#     driver=set_up_browser
#     driver.get("https://www.saucedemo.com/")
#     assert 'Swag Labs'in driver.title
#     print('Pass')
#
# def test_case2(set_up_browser):
#     print('Start case2')
#     driver=set_up_browser
#     driver.get('https://www.baidu.com')
#     assert '百度' in driver.title
#
# def test_case3(set_up_browser):
#     print('Start case3')
#     driver=set_up_browser
#     driver.get('https://www.sogou.com/')
#     assert '搜狗' in driver.title
