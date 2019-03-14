# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import re

dr = webdriver.Firefox()

dr.get("http://passport.weibo.cn/signin/login")
time.sleep(2)

usrname = "tjuarch@163.com"
psword = "weibo8108"

dr.find_element_by_id("loginName").send_keys(usrname)
time.sleep(1)

dr.find_element_by_id("loginPassword").send_keys(psword)
time.sleep(1)

dr.find_element_by_id("loginAction").click()
time.sleep(2)

def user_info(user_id):
    global dr
    url = "http://weibo.cn/" + user_id
    dr.get(url)
    print("*******************")
    print('user infomation')
    
    string_id = '用户id:' + user_id
    print(string_id)
    
    str_list = dr.find_element_by_xpath("//div[@class ='ut']").text.split(' ')
    string_name = 'nickname:' + str_list[0]
    print(string_name)
    
    string_num = dr.find_element_by_xpath("//div[@class='tip2']")
    pattern = r"\d+\.?\d*"
    result = re.findall(pattern, string_num.text)
    print(string_num.text)
    print("\n*******************")
    
    

