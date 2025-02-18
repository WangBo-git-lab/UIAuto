import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utils.logger import setup_logger
from config import DEVICE_NAME, PLATFORM_VERSION, APP_PACKAGE, APP_ACTIVITY, APPIUM_SERVER_URL, IMPLICIT_WAIT_TIME
from page_objects.login import LoginPage
from page_objects.start import StartPage
from page_objects.home_page import HomePage

logger = setup_logger()
class TestIconClick(unittest.TestCase):
    def setUp(self):
        # 设置Appium驱动的配置参数
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = DEVICE_NAME
        options.app_package = APP_PACKAGE
        options.app_activity = APP_ACTIVITY

        # 启动Appium驱动
        self.driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)

        # 隐式等待设置
        self.driver.implicitly_wait(IMPLICIT_WAIT_TIME)

    def main_flow(self):
        StartPage(self.driver).start()
        LoginPage(self.driver).login()

    def test_all_icons_clickable(self):
        logger.info("开始测试首页所有icon是否可点击")

        home_page = HomePage(self.driver)
        all_icons = home_page.get_all_icons()

        for i in range(len(all_icons)):
            try:
                home_page.click_icon(i)
                logger.info(f"成功点击第 {i + 1} 个icon")
            except Exception as e:
                logger.error(f"点击第 {i + 1} 个icon时出错: {e}")
                self.fail(f"点击第 {i + 1} 个icon时出错: {e}")

        logger.info("首页所有icon可点击测试完成")
    def tearDown(self):
        # 关闭应用
        self.driver.quit()
