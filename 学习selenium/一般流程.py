# -*- coding: utf-8 -*-

# http://www.selenium.org.cn/ selenium中文网

from selenium  import webdriver
import time

# 这里采用的是一般浏览器的模式
driver = webdriver.Chrome()

'''也可以用浏览器无头模式
opt = webdriver.ChromeOptions()
opt.set_headless()
driverHeadless = webdriver.Chrome(options=opt)
'''

#driver.get("https://www.python.org/")
driver.get("https://www.baidu.com")

# waiting...
time.sleep(1)

# 搜索
driver.find_element_by_id('kw').send_keys('pycon')
# 找到按钮，并给一个click（）
driver.find_element_by_id('su').click()

# 设置隐式等待
driver.implicitly_wait(5)

# 设置显式等待
# 需要多导入这三个库
# EC是条件，EC.presence_of_element_located后面参数是一个元组，也可以分开写
# EC的方法有很多，可以参阅
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver.get("https://www.csdn.net/")
try:
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, u'首页')))
finally:
    print(driver.find_element_by_link_text('首页').get_attribute('href'))

# 打开新的页面
driver.window_handles #list，列出所有页面的句柄
driver.switch_to_window(driver.window_handles[-1]) #切换到最新打开的页面


# 截屏
driver.save_screenshot('save.png')

# 退出
time.sleep(2)
driver.quit()

