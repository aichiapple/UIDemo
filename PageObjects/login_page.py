

from PageLocators.loginpage_locators import LoginPageLocator as loc
from Common.basepage import BasePage


class LoginPage(BasePage):

    #登录

    def login(self,username,password):
        #输入用户名
        #输入密码
        doc="登录页面"
        self.wait_eleVisible(locator=loc.username_text,doc=doc)
        self.input_text(loc.username_text,username,doc)
        self.input_text(loc.password_text, password, doc)
        self.click_element(loc.login_button,doc)
    #注册

    #记住密码


    #获取错误信息提示
    def get_errMss_from_loginArea(self):
        doc="获取错误信息"
        # 等待错误提示元素出现，并返回结果
        self.wait_eleVisible(locator=loc.errMsg,doc=doc)
        return self.get_text(locator=loc.errSpan,doc=doc)

