#封装基本函数，执行日志，异常处理 ，失败截图
#所有页面的公共部分
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Common.dir_config  as dir_config
import logging
import datetime
class BasePage:
    def __init__(self,driver):
        self.driver=driver
    #等待元素可见
    def wait_eleVisible(self,locator,times=30,poll_frequency=0.5,doc=""):
        """
        :param locator:
        :param times:
        :param poll_frequency:
        :param doc:
        :return:
        """
        logging.info("等待元素{0}可见".format(locator))
        try:
            #获取等待开始的时间
            start=datetime.datetime.now()
            WebDriverWait(self.driver,times,poll_frequency).until(EC.visibility_of_element_located(locator))
            #等待结束的时间
            end=datetime.datetime.now()
            #求一个差值写在日志里
            waittime=(end-start).seconds
            logging.info("{0}等待时间为{1}".format(locator,waittime))
        except:
            logging.exception("等待元素可见失败！")
            #截图 doc为调用该方法的模块方法等信息
            self.save_screenshot(doc)
            raise

    #等待元素存在
    def wait_elePresence(self):
        pass

    #查找元素
    def get_element(self,locator,doc):

        """
        :param locator: 元素的参数{by方法，以及xpath定位描述}
        :param doc: 返回的调用该方法的路径，方便定位问题位置
        :return: 查找到的元素
        """
        logging.info("查找元素：{}".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.info("查找元素失败!!!")
            #截图
            self.save_screenshot(doc)
            raise
        pass

    #点击操作
    def click_element(self,locator,doc=""):
        doc='登录页面登录按钮'
        #找元素
        ele=self.get_element(locator,doc)
        #对元素进行操作
        logging.info("{0}点击元素{1}".format(doc,locator))
        try:
            ele.click()
        except:
            logging.info("元素点击失败！！！")
            self.save_screenshot(doc)
            raise

    #输入操作
    def input_text(self,locator,text,doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        # 对元素进行操作
        logging.info("{0}对元素{1}进行输入数据{2}".format(doc, locator,text))
        try:
            ele.send_keys(text)
        except:
            logging.info("元素输入失败！！！")
            self.save_screenshot(doc)
            raise

    #获取元素的文本内容
    def get_text(self,locator,doc=""):
        #获取元素
        ele=self.get_element(locator, doc)
        try:
            return ele.text
        except:
            logging.info("获取元素内容失败！！！")
            self.save_screenshot(doc)
            raise

    #获取元素的属性
    def get_element_attribute(self,locator,attr,doc=""):
        # 获取元素
        ele = self.get_element(locator, doc)
        try:
            return ele.get_attribute(attr)
        except:
            logging.info("获取元素属性失败！！！")
            self.save_screenshot(doc)
            raise

    #alert的处理
    def alert_action(self,action="accept"):
        pass

    #iframe切换
    def switch_iframe(self,iframe_reference):
        pass

    #上传操作
    def upload_file(self):
        pass
    #截图
    def save_screenshot(self,doc):
        #图片名称  ：模块名——页面名称——操作名称——年-月-日时分秒，png
        #filepath=指的图片保存目录/model（页面功能名称）_当前时间到秒.png
        filePath=dir_config.screenshot_dir+\
                  "/{0}_{1}.png".format(doc,time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime()))
        #截图文件保存在Screenshot目录下
        #driver方法：self.driver.save_screenshot()
        try:
            self.driver.save_screenshot(filePath)
            logging.info("截取网页成功，文件路径为：{0}".format(filePath))
        except:
            logging.exception("截图失败！！")
            raise

