from page_objects.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy

#登录
class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def login(self):
        self.input_text(MobileBy.ID,1,'15137139921')  #输入账号
        self.input_text(MobileBy.ID,1,'xyz1230.')  #输入密码
        self.click_element(MobileBy.ID,1)  #勾选阅读同意
        self.click_element(MobileBy.ID,1)  #点击登录




