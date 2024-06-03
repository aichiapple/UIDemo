from selenium import webdriver
import pytest
from PageObjects.login_page import LoginPage
class Test_login():
    #正向用例，执行成功，用户登录成功
    def test_login_sucess(self):
        lg=LoginPage(self.driver)
        lg.login("qiaort","2024@Set")






