from PageObjects.index_page import IndexPage
from TestDatas import login_datas as LD
import pytest
# 104 切片12 讲jenkins
@pytest.mark.usefixtures("refresh_page")
@pytest.mark.usefixtures("access_web")

class TestLogin:
    #正常用例，登陆成功
    @pytest.mark.parametrize("caseData", LD.successs_data)
    def test_login_2_sucess(self,access_web,caseData):
      #  logging.info("******登录用例，正常场景****")
        #步骤，输入用户名，密码 点击登录
        access_web[1].login(caseData["user"], caseData["passwd"])
        #断言，首页能否找到推出元素
        assert IndexPage(access_web[0]).isExist_logout_ele()
