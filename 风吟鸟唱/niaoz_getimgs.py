# -*- coding: utf-8 -*-
'''
主页网址为 https://niaozhan.me/
论坛模特列表网址为 https://niaoz.net/model-list
author：五味大侠
date：20190316
本模块实现在地址池中搜索图片地址并保存到指定文件夹。
'''

from selenium import webdriver
from time import sleep
import csv
import requests
import os
import random
import threading

# 在模特展示页获取大图的地址信息
def getimgcontent(url, dr):
    '''
    url:模特展示页的url，https://niaoz.net/moko/100001361.html
    dr:webdriver实例
    实现从当前页获取图片地址信息列表,返回图片地址列表
    '''
    res = []
    try:
        dr.get(url)
        # 暂停一下，缓冲缓冲
        for i in range(3):
            n = random.random()
            sleep(n)
            print(f'wait for {n} seconds')
        content = dr.find_element_by_id("content")
        imgs = content.find_elements_by_xpath("//img")
        for i in imgs:
            res.append(i.get_attribute('original'))
        print(res)
        return res
    except:
        with open('errlog.log', 'a') as fp:
            fp.write(f"{url}, get imgcontent error! \n")
        return "get imgcontent error"

# 根据url存储图片文件
def saveimg(url, filepath, imgname):
    '''
    实现把地址下载储存为图片
    '''
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    try:
        response = requests.get(url)
    except:
        with open('errlog.log', 'a') as fp:
            fp.write(f"{url}, get img response error! \n")
        return "get img response error"
    filename = filepath + os.sep + imgname
    try:
        with open(filename, 'wb') as fp:
            fp.write(response.content)
        return None
    except:
        with open('errlog.log', 'a') as fp:
            fp.write(f"{url}, save img error! \n")
        return "save img error"


def main(modelimgurlfile):
    dr = webdriver.Firefox()
    with open(modelimgurlfile, 'r') as fp:
        num = 0
        reader = csv.reader(fp)
        for i in reader:
            modelimgurl = i[0]
            print(modelimgurl)
            imglist = getimgcontent(modelimgurl, dr)
            for imgurl in imglist:
                imgname = dr.title.split('|')[0].split(' ')[0] + str(num) + '.' + imgurl.split(".")[-1]
                num += 1
                filepath = ".\\img"
                print(imgname)
                saveimg(imgurl, filepath, imgname)
    return "ALL DONE!"

def dividecsv():
    with open("modelimgurl.csv", 'r', newline='') as fp:
        reader = csv.reader(fp)
        num = 0
        for line in reader:
            filenum= num // 500
            filename = "modelimgurl" + str(filenum) + ".csv"
            with open(filename, 'a', newline='') as fp2:
                writer = csv.writer(fp2)
                writer.write(line)
            num += 1
    return None
if __name__ == "__main__":
    threads = []
    for i in range(4):
        t = threading.Thread(target=main, args=(f"modelimgurl{i}.csv",))
        threads.append(t)
    for t in threads:
        t.start()
    t.join()





