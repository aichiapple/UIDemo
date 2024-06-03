
from selenium.webdriver.common.by import By


class LoginPageLocator:
    username_text = (By.XPATH, "//*[@id='username']")
    password_text = (By.XPATH, "//*[@id='password']")
    login_button = (By.XPATH, "//*[@class='login-button']")
    errMsg=(By.XPATH, '//*[@class="tip-error"]')
    errSpan=(By.XPATH, '//*[@class="tip-error"]/span/')