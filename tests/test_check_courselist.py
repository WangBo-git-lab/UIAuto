import unittest
from appium import webdriver
from config import DEVICE_NAME, PLATFORM_VERSION, APP_PACKAGE, APP_ACTIVITY, APPIUM_SERVER_URL, IMPLICIT_WAIT_TIME
from page_objects.home_page import HomePage
from utils.logger import setup_logger
from appium.webdriver.common.mobileby import MobileBy

logger = setup_logger()


class TestHomepageSlideClick(unittest.TestCase):
    def setUp(self):
        # 设置Appium驱动的配置参数
        desired_caps = {
            "platformName": "Android",
            "deviceName": DEVICE_NAME,
            "platformVersion": PLATFORM_VERSION,
            "appPackage": APP_PACKAGE,
            "appActivity": APP_ACTIVITY
        }

        # 启动Appium驱动
        self.driver = webdriver.Remote(APPIUM_SERVER_URL, desired_caps)

        # 隐式等待设置
        self.driver.implicitly_wait(IMPLICIT_WAIT_TIME)

    def test_slide_and_click_entry(self):
        logger.info("开始测试首页下滑直至找到入口然后点击的操作")

        home_page = HomePage(self.driver)

        found_element = home_page.swipe_down_until_element_found(MobileBy.ID,1)
        if found_element:
            logger.info("成功找到目标入口元素")
            home_page.click_element(MobileBy.ID,1)
            logger.info("已点击目标入口元素")
        else:
            logger.error("未找到目标入口元素")
            self.fail("未找到目标入口元素")

    def tearDown(self):
        logger.info("关闭Appium驱动")
        self.driver.quit()

