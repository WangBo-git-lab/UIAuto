import os
#adb shell
# 设备相关配置
DEVICE_NAME = "7c1fddbf"  # 实际设备名称或模拟器名称
PLATFORM_VERSION = "14"  # 实际的安卓系统版本

# 应用相关配置
APP_PACKAGE = "cn.jiazhengye.panda_home"  # 待办事项应用的包名
APP_ACTIVITY = "cn.jiazhengye.panda_home.activity.commonactivity.StartActivity"  # 应用的主活动名

# Appium服务器地址
APPIUM_SERVER_URL = "http://127.0.0.1:4723/wd/hub"

# 等待超时时间设置
IMPLICIT_WAIT_TIME = 10
EXPLICIT_WAIT_TIME = 15