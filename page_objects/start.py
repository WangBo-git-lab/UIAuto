from page_objects.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy

#启动
class StartPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def start(self):
        self.wait_for_element_to_be_clickable(MobileBy.ID,1)  #同意服务
        for i in range(4): #左滑4次
            self.swipe_left()
        self.wait_for_element_to_be_clickable(MobileBy.ID,1)  #同意启动

