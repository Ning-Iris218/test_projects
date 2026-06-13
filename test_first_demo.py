import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_first_demo():
    driver= webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    username_filed= driver.find_element(By.ID,'user-name')
    username_filed.send_keys('standard_user')
    password_field=driver.find_element(By.ID,'password')
    password_field.send_keys('secret_sauce')
    button_click=driver.find_element(By.ID,'login-button')
    button_click.click()
    assert 'inventory.html'in driver.current_url
    print('success')
    # price_element=driver.find_element(By.CLASS_NAME,'inventory_item_price')
    # price_text=price_element.text
    # print(price_text)
    # assert price_text=='$29.99'

    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME,'inventory_item_name'))
    )
    button1=driver.find_element(By.ID,'add-to-cart-sauce-labs-backpack')
    button1.click()

    button2=driver.find_element(By.CLASS_NAME,'shopping_cart_link')
    button2.click()

    WebDriverWait(driver,10).until(EC.url_contains('cart.html'))
    bag1=driver.find_element(By.CLASS_NAME,'inventory_item_name')
    bag1_text=bag1.text
    print(bag1_text)
    assert 'Sauce Labs Backpack'in bag1_text

    time.sleep(3)
    driver.quit()