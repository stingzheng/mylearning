# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 21:23:50 2019

@author: zhaoguang
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
import time, csv

def writecsv(sth, filename): # 数据写入csv文件
    with open(filename, 'w') as fp:
        writer = csv.writer(fp)
        try:
            writer.writerow(sth)
        except:
            print('ERR!')
    return None

# 设置显示等待的库
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 设置无头浏览器模式
#opt = webdriver.ChromeOptions()
#opt.set_headless()
#dr_hl = webdriver.Chrome(option=opt)

dr = webdriver.Chrome()
dr.get("http://top.baidu.com/")

hw_dict = []

# 搜索并打印网页的头条新闻关键词
for i in range(1,11):
    xpath = '//*[@id="hot-list"]/li['+str(i)+']/a[1]'
    value = dr.find_element_by_xpath(xpath).get_attribute('title')
    hw_dict.append(value)

URL = f'https://www.toutiao.com/search/?keyword={hw_dict[0]}'
dr.get(URL)

xpath = '//*[@id="J_section_0"]/div/div/div[1]/div/div[1]/a/span'

# 显式等待调用
try:
    WebDriverWait(dr, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath)))
    # 注意：EC.presence_of_element_located的参数是一个元组
finally:
    dr.find_element_by_xpath(xpath).click()

