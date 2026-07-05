import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class Information_Page:
    _FIRST_NAME=(By.ID,'first-name')
    _LAST_NAME=(By.ID,'last-name')
    _POST_CODE=(By.ID,'postal-code')
    _CONTINUE_BUTTON=(By.ID,'continue')

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def fill_info(self, first_name, last_name, postal_code):
        # 第一步：把三个输入框在底层 HTML 里的真身揪出来
        fn = self.wait.until(EC.presence_of_element_located(self._FIRST_NAME))
        ln = self.wait.until(EC.presence_of_element_located(self._LAST_NAME))
        pc = self.wait.until(EC.presence_of_element_located(self._POST_CODE))

        # ⚛️ 第二步：专门对付 React 框架的“底层注射器” JS 代码
        react_hack_js = """
            let input = arguments[0];
            let value = arguments[1];
            
            // 1. 绕过 React 的拦截，调用浏览器最底层的 HTML 接口强行把字塞进去
            let nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
            nativeSetter.call(input, value);
            
            // 2. 伪造一个原生的 input 事件派发出去，骗过 React 框架："嘿！真人刚刚敲击了键盘，快更新！"
            input.dispatchEvent(new Event('input', { bubbles: true }));
        """

        # 第三步：对三个框分别执行这套 JS 注射操作！绝对不可能填不进去！
        self.driver.execute_script(react_hack_js, fn, first_name)
        self.driver.execute_script(react_hack_js, ln, last_name)
        self.driver.execute_script(react_hack_js, pc, postal_code)

    def click_continue(self):
        btn = self.wait.until(EC.presence_of_element_located(self._CONTINUE_BUTTON))

        self.driver.execute_script("arguments[0].click();", btn)

        try:
            self.wait.until(EC.url_contains("step-two"))
        except TimeoutException:
            self.driver.save_screenshot("github_error_screenshot.png")
            raise
