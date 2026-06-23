from selenium.webdriver.common.by import By

class LoginPage:
    _USERNAME_INPUT=(By.ID,'user-name')
    _PASSWORD_INPUT=(By.ID,'password')
    _LOGIN_BUTTON=(By.ID,'login-button')

    def __init__(self,driver):
        self.driver=driver

    def login(self,username,password):
        self.driver.find_element(*self._USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self._PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self._LOGIN_BUTTON).click()
