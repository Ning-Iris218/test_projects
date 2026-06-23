import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_practice2():
    driver = webdriver.Chrome()
    driver.get('https://the-internet.herokuapp.com/tables')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#table1 tbody tr td:nth-child(3)'))
    )
    all_mails=driver.find_elements(By.CSS_SELECTOR, '#table1 tbody tr td:nth-child(3)')
    for x in all_mails:
        mail=x.text
        assert "@" in mail
        assert mail.endswith('.com') or mail.endswith('.net')
        print(f'{mail}')

    time.sleep(3)
    driver.quit()
