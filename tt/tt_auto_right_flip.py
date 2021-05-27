import os
import random

from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "xxx",
  "appPackage": "com.p1.mobile.putong",
  "appActivity": ".ui.splash.SplashProxyAct",
    # "appPackage": "com.fenzotech.jimu",
    # "appActivity": "com.eomchat.module.splash.SplashActivity",
  "unicodeKeyboard": False,
  "resetKeyboard": True,
  "noReset": True,
  "newCommandTimeout": 6000,
  "automationName": "UiAutomator2"
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 设置缺省等待时间
# driver.implicitly_wait(5)

# 如果有`新版本按钮`界面，点击`取消`
cancel_button = driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.TextView")
if cancel_button[0]:
    cancel_button[0].click()

# 根据id定位搜索位置框，点击
# driver.find_element_by_id("expand_search").click()
i = 0;
while(i < 300):
    k = random.randint(0,100);
    randomY = str(500 + random.randint(0, 200)) + " "
    randomX1 = str(100 + random.randint(0, 100)) + ' '
    randomX2 = str(300 + random.randint(0, 100)) + ' '
    if ( k < 79):
        right = 'adb shell input swipe ' + randomX1 + randomY + randomX2 + randomY + str(random.randint(100, 300))
        os.system(right)
    else:
        left = 'adb shell input swipe ' + randomX2 + randomY + randomX1 + randomY + str(random.randint(100, 300))
        os.system(left)
    i += 1;
    print(i)