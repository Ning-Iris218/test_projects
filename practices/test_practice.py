import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_practice_1():
    driver= webdriver.Chrome()
    driver.get('https://the-internet.herokuapp.com/challenging_dom')

    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'td:nth-child(1)'))
    )
    all_cells=driver.find_elements(By.CSS_SELECTOR,'td:nth-child(1)')
    for x in all_cells:
        files=x.text
        assert files[-1].isdigit()
        print(f'{files}')


    print("success")
    time.sleep(3)
    driver.quit()


