# -*- coding: utf-8 -*-
'''
主页网址为 https://niaozhan.me/
论坛模特列表网址为 https://niaoz.net/model-list
author：五味大侠
date：20190316
哈哈哈，模特照片，微艺术。。。。你懂得
'''


from selenium import webdriver
from time import sleep
import csv
import random


modellistpage = "https://niaoz.net/model-list"

dr = webdriver.Firefox()


def get_modelpage_list(url, dr):
    '''
    url:the page tobe scraped
    dr:instance of webdriver
    实现从模特列表获取各位model的主页地址，并存在csv文件中。
    '''
    dr.get(modellistpage)
    tag_list = dr.find_elements_by_xpath("//li[@id]")
    #print("taglist",tag_list)
    fp = open('modelpagelist.csv', 'w', newline='')
    writer = csv.writer(fp)
    for i in tag_list:
        print(i)
        modellist = i.find_elements_by_xpath("a[@title]")
        for j in modellist:
            item = j.get_attribute('href')
            writer.writerow([item])
            print(item)
    fp.close()
    dr.close()
    return None


def get_modelimg_list(url, dr):
    '''
    实现从模特主页获取模特展示页的地址列表，并存在csv文件中。
    '''
    dr.get(url)
    with open("modelimgurl.csv", 'a', newline='') as fp2:
        writer = csv.writer(fp2)
        blocklist = dr.find_element_by_class_name("block-list")
        items = blocklist.find_elements_by_xpath("/html/body/div[3]/div/div[2]/div/div[3]/div/a[@href]")
        for j in items:
            item = j.get_attribute('href')
            writer.writerow([item])
            print(item)
        for i in range(3):
            n = random.random() * 2
            sleep(n)
            print(f'wait for {n} seconds')
    return None


with open("modelpagelist.csv", 'r') as fp:
    reader = csv.reader(fp)
    for i in reader:
        modelhomeurl = i[0]
        try:
            get_modelimg_list(modelhomeurl, dr)
        except:
            with open("error.log", 'a') as fperr:
                fperr.write(f"{modelhomeurl} is error!\n")
            continue










