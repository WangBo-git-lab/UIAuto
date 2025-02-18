from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import subprocess


class BasePage:
    def __init__(self, driver):
        """
        构造函数：初始化页面对象

        参数:
        - driver: 浏览器驱动实例，用于与浏览器进行交互
        """
        self.driver = driver

    def find_element(self, by, value):
        """
        在当前驱动实例中查找单个元素。

        :param by: 元素的定位方式，如id、class_name、xpath等。
        :param value: 与定位方式对应的值。
        :return: 返回找到的元素对象。
        """
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        """
        在当前驱动对象中通过指定的查找方式和值来定位一组元素。

        参数:
        - by: 定位元素的方式，例如通过ID、类名、XPath等。
        - value: 基于所选定位方式的值，用于具体定位元素。

        返回:
        - 一组元素对象，如果找不到元素，则返回空列表。
        """
        return self.driver.find_elements(by, value)

    def click_element(self, by, value):
        """
        点击页面上的一个元素。

        该函数通过使用提供的定位方法（by）和定位值（value）来查找页面上的一个元素，并对其进行点击操作。
        这在自动化测试中通常用于模拟用户点击按钮、链接等操作。

        参数:
        - by: 用于定位元素的方法，例如id、class_name、xpath等。
        - value: 元素的定位值，根据定位方法而定。

        返回值:
        无
        """
        # 查找页面上的元素
        element = self.find_element(by, value)
        # 对找到的元素执行点击操作
        element.click()

    def input_text(self, by, value, text):
        """
        向指定的页面元素输入文本。

        此方法首先根据给定的定位策略（by）和定位值（value）找到页面上的一个元素，
        然后向该元素发送指定的文本，常用于网页表单的自动填充。

        参数:
        - by: 定位策略，如XPath, ID, CSS选择器等。
        - value: 定位值，即使用定位策略的具体值。
        - text: 要输入的文本，将被发送到找到的元素。

        返回:
        无
        """
        # 找到指定的页面元素
        element = self.find_element(by, value)
        # 向找到的元素输入指定的文本
        element.send_keys(text)

    def get_element_text(self, by, value):
        """
        根据指定的查找方式和值获取页面元素的文本。

        此方法首先使用传入的查找方式（by）和值（value）定位到页面上的一个元素，
        然后返回该元素的文本内容。常用于需要提取页面上特定元素的文本信息的场景。

        参数:
        by (str): 元素的查找方式，如XPath、ID、CSS选择器等。
        value (str): 查找方式对应的值，用于定位具体的元素。

        返回:
        str: 定位到的元素的文本内容。如果没有找到元素或元素没有文本，则返回空字符串。
        """
        # 定位页面元素
        element = self.find_element(by, value)
        # 返回元素的文本内容
        return element.text

    def clear_element_text(self, by, value):
        """
        清空指定元素的文本内容。

        该方法通过传入的定位策略（by）和定位值（value）找到页面上的元素，并清空该元素的文本内容。
        主要用于表单元素的重置或更新。

        参数:
        - by: 定位策略，如XPath, ID, CSS Selector等。
        - value: 定位值，即通过指定的定位策略找到元素的具体表达式。

        返回值:
        无
        """
        # 查找指定的元素
        element = self.find_element(by, value)
        # 清空找到的元素的文本内容
        element.clear()

    def wait_for_element_to_be_clickable(self, by, value, timeout=10):
        """
        等待元素可被点击

        该函数会尝试寻找一个网页元素，直到该元素出现并可被点击为止
        如果在规定时间内元素没有出现或不可点击，将抛出异常

        参数:
        by (str): 定位元素的方法，如XPath、ID等
        value (str): 元素的值，与定位方法对应
        timeout (int): 最长等待时间，默认为10秒

        返回:
        WebElement: 可点击的网页元素

        抛出:
        Exception: 如果元素定位失败或超时，抛出异常
        """
        try:
            # 初始化WebDriverWait对象，设置最大等待时间为timeout秒
            wait = WebDriverWait(self.driver, timeout)
            # 使用until方法等待元素可点击，并返回该元素
            return wait.until(EC.element_to_be_clickable((by, value)))
        except:
            # 如果发生异常，抛出元素定位失败的异常
            raise Exception('元素定位失败')

    def wait_for_element_to_be_visible(self, by, value, timeout=10):
        """
        等待页面上的元素可见。

        该方法主要用于等待页面上的某个元素在指定时间内变得可见。这对于页面加载或动态内容加载时确保元素可用性非常有用。

        参数:
        - by: 用于定位元素的方法，例如XPath、CSS选择器等。
        - value: 元素定位方法的具体值。
        - timeout: 超时时间（秒），在此时间内如果元素未变为可见，则抛出异常。默认为10秒。

        返回值:
        - 返回找到的元素对象。
        """
        # 创建WebDriverWait实例，使用driver和指定的超时时间。
        wait = WebDriverWait(self.driver, timeout)
        # 使用until方法等待条件满足，即元素可见。
        return wait.until(EC.visibility_of_element_located((by, value)))

    def swipe_up(self, duration=1000):
        """
        在屏幕上执行上滑操作。

        此函数通过获取当前窗口的大小，计算出上滑操作的起始和结束坐标，然后调用webdriver的swipe方法执行上滑。
        上滑操作从屏幕底部中央开始，到屏幕顶部中央结束，以此模拟用户的手指上滑操作。

        参数:
        duration (int): 上滑操作持续的时间，以毫秒为单位。默认值为1000毫秒（1秒）。
        """
        # 获取当前屏幕的大小
        screen_size = self.driver.get_window_size()

        # 计算上滑操作的起始坐标：屏幕宽度的0.5倍（中央），屏幕高度的0.8倍（接近底部）
        start_x = screen_size['width'] * 0.5
        start_y = screen_size['height'] * 0.8

        # 计算上滑操作的结束坐标：屏幕宽度的0.5倍（中央），屏幕高度的0.2倍（接近顶部）
        end_x = screen_size['width'] * 0.5
        end_y = screen_size['height'] * 0.2

        # 调用webdriver的swipe方法执行上滑操作
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def swipe_down(self, duration=1000):
        """
        在屏幕上演示向下滑动的操作。

        此函数通过获取当前窗口的大小来计算滑动的起始和结束坐标，
        然后调用swipe方法执行滑动操作。向下滑动是从屏幕上部中间位置
        到下部中间位置的滑动。

        参数:
        - duration: 滑动操作持续的时间，以毫秒为单位。默认值为1000毫秒（1秒）。

        返回值:
        此函数没有返回值。
        """
        # 获取当前窗口的大小
        screen_size = self.driver.get_window_size()

        # 计算滑动的起始和结束坐标
        start_x = screen_size['width'] * 0.5
        start_y = screen_size['height'] * 0.2
        end_x = screen_size['width'] * 0.5
        end_y = screen_size['height'] * 0.8

        # 执行滑动操作
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def swipe_left(self, duration=1000):
        """
        在屏幕上执行向左滑动的操作。

        :param duration: 滑动操作持续的时间，以毫秒为单位，默认为1000毫秒（1秒）。
        """
        # 获取当前屏幕的尺寸信息
        screen_size = self.driver.get_window_size()

        # 计算滑动操作的起始和结束坐标
        start_x = screen_size['width'] * 0.8
        start_y = screen_size['height'] * 0.5
        end_x = screen_size['width'] * 0.2
        end_y = screen_size['height'] * 0.5

        # 执行从右向左的滑动操作
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def swipe_right(self, duration=1000):
        """
        在屏幕上执行向右滑动的操作。

        :param duration: 滑动操作持续的时间，以毫秒为单位，默认为1000毫秒（1秒）。
        """
        # 获取当前屏幕的尺寸信息
        screen_size = self.driver.get_window_size()

        # 计算滑动起始点的x坐标，位于屏幕宽度的20%
        start_x = screen_size['width'] * 0.2
        # 计算滑动起始点和结束点的y坐标，位于屏幕高度的50%，因为是向右滑动，所以y坐标不变
        start_y = screen_size['height'] * 0.5
        end_y = screen_size['height'] * 0.5

        # 计算滑动结束点的x坐标，位于屏幕宽度的80%
        end_x = screen_size['width'] * 0.8

        # 执行从左到右的滑动操作，duration参数定义了滑动的持续时间
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def long_press_element(self, element):
        """
        执行长按元素的操作。

        通过TouchAction类初始化动作对象，并对指定元素执行长按操作。

        参数:
        - element: 要长按的元素。

        返回值:
        无
        """
        # 初始化TouchAction对象，传入driver作为参数
        actions = TouchAction(self.driver)
        # 对指定的element执行长按操作，并触发（perform）
        actions.long_press(element).perform()

    def zoom_in(self):
        """
        使用双指缩放手势来放大屏幕。

        此方法通过模拟两个手指在屏幕上移动来实现放大效果。它首先确定屏幕的中心点，
        然后定义两个手指的起始和结束位置。两个手指从屏幕的对角线方向向中心移动，
        以实现缩放效果。
        """
        # 获取当前窗口的尺寸
        screen_size = self.driver.get_window_size()

        # 计算屏幕中心点的坐标
        anchor_x = screen_size['width'] * 0.5
        anchor_y = screen_size['height'] * 0.5

        # 第一个手指的起始位置，略偏左上角
        finger1_start_x = screen_size['width'] * 0.4
        finger1_start_y = screen_size['height'] * 0.4

        # 第二个手指的起始位置，略偏右下角
        finger2_start_x = screen_size['width'] * 0.6
        finger2_start_y = screen_size['height'] * 0.6

        # 第一个手指的结束位置，更靠近左上角
        finger1_end_x = screen_size['width'] * 0.3
        finger1_end_y = screen_size['height'] * 0.3

        # 第二个手指的结束位置，更靠近右下角
        finger2_end_x = screen_size['width'] * 0.7
        finger2_end_y = screen_size['height'] * 0.7

        # 创建一个TouchAction对象来模拟触摸手势
        action = TouchAction(self.driver)

        # 模拟两个手指的缩放手势
        action.press(x=finger1_start_x, y=finger1_start_y).wait(1000).move_to(x=finger1_end_x, y=finger1_end_y). \
            press(x=finger2_start_x, y=finger2_start_y).wait(1000).move_to(x=finger2_end_x, y=finger2_end_y). \
            release().perform()

    # 根据指定的查找方式和值，向下滑动直到找到元素
    # 此函数用于在移动应用自动化测试中，处理需要通过滑动来查找元素的场景
    def swipe_down_until_element_found(self, by, value):
        # 进入一个无限循环，直到找到元素或发生异常
        while True:
            try:
                # 尝试根据提供的查找方式和值找到元素
                element = self.find_element(by, value)
                # 如果元素成功找到，返回该元素，结束循环
                return element
            except:
                # 如果在当前屏幕未找到元素，则执行向下滑动操作，以显示更多内容
                self.swipe_down()

    def go_back(self):
        """
        使driver返回到前一个页面。
        """
        self.driver.back()

    #验证元素是否存在
    def assert_element_exists(self, by, value, timeout=10):
        try:
            # 使用WebDriverWait等待元素出现，超时时间为timeout秒
            wait = WebDriverWait(self.driver, timeout)
            # 返回等待结果，如果在指定时间内找到元素，则返回该元素
            return wait.until(EC.presence_of_element_located((by, value)))
        except:
            # 如果元素未找到，捕获异常并抛出断言错误，提示元素不存在
            raise AssertionError("元素不存在")


    def assert_element_text(self, by, value, expected_text):
        """
        断言元素的文本是否与预期文本一致

        参数:
        by: 定位元素的方法，如XPath、ID等
        value: 元素的值，与定位方法对应的具体值
        expected_text: 预期的元素文本

        异常:
        如果元素文本与预期文本不一致，抛出AssertionError异常
        """
        # 查找元素并获取其文本内容
        actual_text = self.find_element(by,value)

        # 比较实际文本与预期文本，如果不一致则抛出异常
        if actual_text != expected_text:
            raise AssertionError(f"元素文本与预期不符，实际为{actual_text}，预期为{expected_text}")

    def take_screenshot(self, screenshot_dir, screenshot_name):
        """
        截取屏幕并保存截图。

        该方法主要用于自动化测试过程中，当需要获取当前屏幕的截图时调用。它会检查指定的目录是否存在，
        如果不存在则创建该目录，然后将截图保存到指定路径。

        参数:
        screenshot_dir (str): 保存截图的目录路径。
        screenshot_name (str): 截图文件的名称。

        返回:
        无
        """
        # 检查截图目录是否存在，如果不存在则创建
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        # 组合截图的完整路径
        screenshot_path = os.path.join(screenshot_dir, screenshot_name)

        # 使用webdriver的截图功能，将当前屏幕内容保存为图片文件
        self.driver.get_screenshot_as_file(screenshot_path)

    def accept_alert(self):
        """
        接受并处理警告对话框。

        该方法用于在自动化测试过程中，当出现警告对话框时，通过调用此方法来确认或接受该对话框。
        这在测试中很有用，因为它可以帮助处理预期的警告，确保测试能够顺利进行。

        参数:
        无

        返回:
        无
        """
        # 切换到警告对话框
        alert = self.driver.switch_to.alert
        # 确认警告对话框
        alert.accept()

    def dismiss_alert(self):
        """
        关闭当前页面上的警告框。

        该方法假设当前网页上存在一个警告框。它首先将驱动程序的焦点切换到警告框，然后关闭它。
        """
        # 将驱动程序的焦点切换到警告框
        alert = self.driver.switch_to.alert
        # 关闭警告框
        alert.dismiss()


    def get_alert_text(self):
        """
        切换到弹窗并获取其文本内容。

        此方法用于处理弹窗消息，通过切换到弹窗，能够读取弹窗中的文本内容，
        以便进一步处理或断言。

        Returns:
            str: 弹窗中的文本内容。
        """
        # 切换到弹窗
        alert = self.driver.switch_to.alert
        # 返回弹窗的文本内容
        return alert.text

    def hide_keyboard(self):
        """
        隐藏键盘。

        在移动应用自动化测试中，此方法用于隐藏当前界面的键盘。这对于恢复屏幕显示的正常状态或执行其他操作是必要的。
        """
        self.driver.hide_keyboard()


    def get_device_info(self):
        """
        获取设备信息。

        通过执行移动设备的脚本命令来收集设备信息。

        :return: 设备信息字典，包含设备的各种属性。
        """
        # 执行移动设备的脚本命令来收集设备信息
        device_info = self.driver.execute_script("mobile: deviceInfo")
        # 返回收集到的设备信息
        return device_info

    def check_device_network_status(self):
        """
        检查设备的网络连接状态。

        该方法通过执行移动设备上的脚本获取当前的网络连接状态，主要用于自动化测试场景中判断设备是否具有网络连接。

        Returns:
            network_status: 字典，包含设备当前的网络连接信息。
        """
        # 执行移动设备上的脚本以获取网络连接状态
        network_status = self.driver.execute_script("mobile: networkConnection")

        # 返回获取到的网络状态信息
        return network_status

    def check_app_permission(self, permission):
        """
        检查应用程序是否被授予了指定的权限。

        通过调用ADB命令`pm check-permission`来检查权限，这是针对Android设备的方法。

        参数:
        permission (str): 需要检查的应用程序权限名称。

        返回:
        bool: 如果应用程序被授予了指定的权限，则返回True，否则返回False。
        """
        # 获取当前应用的包名，用于后续的权限检查。
        app_package = self.driver.current_package

        # 构建ADB命令，用于检查指定权限是否被授予。
        command = f"adb shell pm check-permission -u 0 {permission} {app_package}"

        # 执行ADB命令并获取输出结果，使用strip()移除可能的换行符或空白字符。
        result = subprocess.check_output(command, shell=True).decode("utf-8").strip()

        # 检查输出结果中是否包含"granted"，以判断权限是否被授予。
        return "granted" in result

    def grant_app_permission(self, permission):
        """
        为当前应用授予指定权限。

        该方法使用ADB命令为设备上的当前应用授予特定的权限。这对于测试或配置应用的运行环境非常有用，
        尤其是在需要手动干预或在自动化脚本中处理权限管理时。

        参数:
        - permission (str): 需要授予应用的权限字符串，例如 'android.permission.INTERNET'。

        返回:
        该方法没有返回值。如果命令执行成功，意味着权限被成功授予，否则可能会有错误输出在控制台中。
        """
        # 获取当前应用的包名，以便在ADB命令中指定目标应用
        app_package = self.driver.current_package

        # 构建ADB命令，用于授予应用指定的权限
        command = f"adb shell pm grant {app_package} {permission}"

        # 执行ADB命令，为应用授予指定的权限
        subprocess.call(command, shell=True)

    #撤销权限
    def revoke_app_permission(self, permission):
        # 获取当前应用的包名
        app_package = self.driver.current_package
        # 构建撤销权限的adb命令
        command = f"adb shell pm revoke {app_package} {permission}"
        # 执行adb命令撤销权限
        subprocess.call(command, shell=True)


    def clear_app_cache(self):
        """
        清除当前应用的缓存数据。

        该方法首先获取当前正在操作的应用包名，然后构造一条ADB命令，
        用于清除该应用的缓存数据。执行命令是通过调用`subprocess.call`完成的，
        以实现自动化清除缓存的功能。
        """
        # 获取当前应用的包名
        app_package = self.driver.current_package

        # 构造清除缓存的ADB命令
        command = f"adb shell pm clear {app_package}"

        # 执行清除缓存的命令
        subprocess.call(command, shell=True)

    def get_app_storage_path(self):
        """
        获取当前应用的存储路径。

        该方法使用ADB命令来获取应用的存储路径。它首先获取当前应用的包名，
        然后构造一个ADB命令来查询该应用的存储路径，并解析命令的输出以获取路径。

        Returns:
            str: 应用的存储路径。
        """
        # 获取当前应用的包名
        app_package = self.driver.current_package

        # 构造ADB命令来获取应用的存储路径
        command = f"adb shell pm path {app_package}"

        # 执行ADB命令并解析输出
        result = subprocess.check_output(command, shell=True).decode("utf-8").strip()

        # 返回应用的存储路径
        return result

    def write_data_to_local_storage(self, key, value):
        """
        将数据写入本地存储。

        此方法模拟了一个应用中将数据写入本地存储的操作。虽然具体的元素定位和操作方式
        取决于应用的实际实现，但这里假设存在一个界面，通过该界面用户可以输入键值对并保存
        到本地存储中。

        参数:
        key (str): 要写入本地存储的数据的键。
        value (str): 与键关联的值。

        返回:
        无
        """
        # 假设应用有一个通过元素操作来写入本地存储的接口
        # 这里需要根据应用实际情况修改具体操作
        input_key_element = self.find_element(MobileBy.ID, "local_storage_key_input")
        input_value_element = self.find_element(MobileBy.ID, "local_storage_value_input")
        save_button_element = self.find_element(MobileBy.ID, "local_storage_save_button")

        # 向键输入框发送键值
        input_key_element.send_keys(key)
        # 向值输入框发送值
        input_value_element.send_keys(value)
        # 点击保存按钮以将数据保存到本地存储
        save_button_element.click()

    def read_data_from_local_storage(self, key):
        """
        从本地存储中读取数据。

        该方法通过模拟用户操作应用界面来读取本地存储中的数据。它假设应用界面有相应的输入框和按钮
        用于指定要读取的键以及显示读取结果。

        参数:
        key (str): 要从本地存储中读取的数据的键。

        返回:
        str: 从本地存储中读取的数据，以字符串形式返回。
        """
        # 假设应用有一个通过元素操作来读取本地存储的接口
        # 这里需要根据应用实际情况修改具体操作
        input_key_element = self.find_element(MobileBy.ID, "local_storage_key_input")
        read_button_element = self.find_element(MobileBy.ID, "local_storage_read_button")
        input_key_element.send_keys(key)
        read_button_element.click()
        result_element = self.find_element(MobileBy.ID, "local_storage_result_display")
        return result_element.text









