from page_objects.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    #找到所有icon
    def get_all_icons(self):
        return self.find_elements(MobileBy.CLASS_NAME, "icon_class_name")  # 替换为实际的icon类名

    #点击所有icon
    def click_icon(self, icon_index):
        icons = self.get_all_icons()
        if icon_index < len(icons):
            icons[icon_index].click()
        else:
            raise IndexError("无效的icon索引")

