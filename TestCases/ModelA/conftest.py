


import pytest
from selenium import webdriver

from TestDatas import Common_Datas as CD
from PageObjects.login_page import LoginPage
driver=None
@pytest.fixture(scope="class")
def access_web():
    global driver
    #前置操作
    print("===========所有测试之前，setup===整个测试类只执行一次====")
    # 1.创建Edge浏览器对象，这会在电脑上在打开一个浏览器窗口
    driver = webdriver.Edge()
    # 2.通过浏览器向服务器发送URL请求
    driver.get(CD.web_login_url)
    lg=LoginPage(driver)
    yield (driver,lg)
    # 后置操作
    print("===========所有测试之后，teardown===整个测试类只执行一次====")
    driver.quit()

@pytest.fixture(scope="function")
def refresh_page():
    global driver
    #前置操作
    yield
    #后置操作
    driver.refresh()

