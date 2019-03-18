# -*- coding: utf-8 -*-
'''
网址类似http://www.tjlandmarket.com/notice/view_page/8ad5013511b24d33aa8fc02c82a982b1.html
从每块地的页面中抓取有用的土地出让信息，每块地存成一个txt文件，后续再提取有用的信息
'''
from selenium import webdriver
from time import sleep
import random
import csv
import os
import time
import threading

def getinfo(url, dr):
    '''
    根据地址摘取有用的信息
    正确情况下返回：filename, landinfo
    错误情况下返回：-1，并且写入错误文档
    '''
    try:
        dr.get(url)
    except:
        with open('errlog.log', 'a') as fp:
            fp.write(f"{url} 网页打开错误！")
        return -1
    try:
        title = dr.find_element_by_xpath("//h4").text
    except:
        filename = str(time.time())
    filename = title + ".txt"
    try:
        content = dr.find_element_by_xpath("//dl")
    except:
        with open('errlog.log', 'a') as fp:
            fp.write(f"{url} 信息获取错误！")
        return -1
    landinfo = content.text
    return (filename, landinfo)


def writelandinfo(filepath, filename, landinfo):
    '''
    把收到的每块地路径、名称、土地信息写入文件
    '''
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    name = filepath + os.sep + filename
    try:
        with open(name, 'w') as fp:
            fp.write(landinfo)
        return 0
    except:
        return -1

def main(csvname):
    dr = webdriver.Firefox()
    fp = open(csvname, 'r')
    reader = csv.reader(fp)
    for i in reader:
        # 暂停一下，缓冲缓冲
        for _ in range(3):
            n = random.random() * 2
            print(f'wait for {n} seconds')
            sleep(n)
        url = i[0]
        print(f"当前解析页面{url}")
        res = getinfo(url, dr)
        if res != -1:
            a = writelandinfo(".\\landinfo", res[0], res[1])
            if a == 0:
                print('写入成功')
            else:
                print('写入失败')
        else:
            print("网页或者地块错误！")
            continue
    return 0

def dividecsv(csvfile):
    with open(csvfile, 'r', newline='') as fp:
        reader = csv.reader(fp)
        num = 0
        for line in reader:
            filenum= num // 1000
            filename = csvfile.split('.')[0] + str(filenum) + ".csv"
            with open(filename, 'a', newline='') as fp2:
                writer = csv.writer(fp2)
                writer.writerow(line)
            num += 1
    return None



if __name__ == "__main__":
#    threads = []
    for i in range(7):
        t = threading.Thread(target=main, args=(f"landurls{i}.csv",))
        t.start()
    t.join()



