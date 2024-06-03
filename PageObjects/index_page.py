
from Common.basepage import BasePage
from PageLocators.indexPageLocator import IndexPageLocator as loc

class IndexPage(BasePage):

    def isExist_logout_ele(self):
        #等待10s，元素有没有出现登录成功后的默认头像 如果存在就返回true，否则就返回false
        doc='判断是否出现用户登录成功后的头像'
        try:
            ele=self.wait_eleVisible(locator=loc.userDefaultImage,doc=doc)
            return True
        except:
            return False

