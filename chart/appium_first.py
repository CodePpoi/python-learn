import random

from appium import webdriver
import numpy
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '9', # 手机安卓版
  'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.p1.mobile.putong', # 启动APP Package名称
  'appActivity': '.ui.splash.SplashProxyAct', # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator1'
  # 'app': r'd:\apk\bili.apk',
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# 设置缺省等待时间
driver.implicitly_wait(5)

x = driver.get_window_size()['width']
y = driver.get_window_size()['height']

screen = (x,y)
# androidsdk的位置改了，可能会报错，具体会报啥错，自己想想
# 如果有`青少年保护`界面，点击`我知道了`
iknow = driver.find_elements_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.TextView")
# if iknow:
iknow[0].click()
i = 0

# 根据id定位搜索位置框，点击
while i < 268:
  i += 1
  # driver.find_element_by_id("image").click()
  if random.randint(0, 99) > 69:
    driver.swipe(screen[0] * 0.75, screen[1] * 0.5, screen[0] * 0.25, screen[1] * 0.5, (156 + numpy.random.randint(1, 10)) * numpy.random.randint(2, 6))
  else:
    driver.swipe(screen[0] * 0.25, screen[1] * 0.5, screen[0] * 0.75, screen[1] * 0.5, (156 + numpy.random.randint(1, 10)) * numpy.random.randint(2, 6))
    # 根据id定位搜索输入框，点击
  # sbox = driver.find_element_by_xpath("//*[@resource-id='com.p1.mobile.putong.core:id/like']")
  # sbox.click()

  # sbox.send_keys('白月黑羽')
  # # 输入回车键，确定搜索
  # driver.press_keycode(AndroidKey.ENTER)
  #
  # # 选择（定位）所有视频标题
  # eles = driver.find_elements_by_id("title")
  #
  # for ele in eles:
  #     # 打印标题
  #     print(ele.text)

  # input('**** Press to quit..')
driver.quit()



