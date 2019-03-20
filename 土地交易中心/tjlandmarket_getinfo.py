# -*- coding: utf-8 -*-
'''
网址类似http://www.tjlandmarket.com/notice/view_page/8ad5013511b24d33aa8fc02c82a982b1.html
从每块地的页面中抓取有用的土地出让信息，每块地存成一个txt文件，后续再提取有用的信息
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    print('='*10 + "正在打开网页" + '='*13)
    dr.get(url)
    # 增加了显示等待，超时时间10秒，没有找到网页尾部的元素。
    try:
        WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "footer")))
        print('='*10 + "网页加载---正常" + '='*10)
    except:
        print('='*10 + "网页加载---错误" + '='*10)
        with open('errlog.log', 'a') as fp:
            fp.write(f"{url} 网页加载错误！\n")
        return -1
    try:
        print('='*10 + "获取标题" + '='*17)
        title = dr.find_element_by_xpath("//h4").text
        print('='*10 + "获取标题---成功" + '='*10)
    except:
        print('='*10 + "获取标题失败，随便取个名字" + '='*17)
        filename = str(time.time())
    filename = title + ".txt"
    try:
        print('='*10 + "获取内容" + '='*17)
        content = dr.find_element_by_xpath("//dl")
        print('='*10 + "获取内容---成功" + '='*10)
    except:
        print('='*10 + "获取内容---错误" + '='*10)
        with open('errlog.log', 'a') as fp:
            fp.write(f"{url} 获取内容错误！\n")
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
        print('='*10 + "创建文件" + '='*17)
        with open(name, 'w') as fp:
            fp.write(landinfo)
        print('='*10 + "写入文件---成功" + '='*10)
        # 增加一个完成比例
        total = 6066
        rate = str(len(os.listdir(".\\landinfo")) / total * 100)[:5] + '%'
        print('='*40 + f"已完成 {rate}")
        return 0
    except:
        print('='*10 + "写入文件---失败" + '='*10)
        with open('errlog.log', 'a') as fp:
            fp.write(f"{name} 写入失败！\n")
        return -1


def main(csvname):
    dr = webdriver.Firefox()
    fp = open(csvname, 'r')
    reader = csv.reader(fp)
    for i in reader:
        url = i[1]
        print(f"当前解析页面：\n{url}")
        res = getinfo(url, dr)
        if res != -1:
            writelandinfo(".\\landdiff", res[0], res[1])
        else:
            continue
        # 暂停一下，缓冲缓冲
        for _ in range(3):
            n = random.random() * 2
            print(f'wait for {n} seconds')
            sleep(n)
    return 0


def dividecsv(csvfile):
    with open(csvfile, 'r', newline='') as fp:
        reader = csv.reader(fp)
        num = 0
        for line in reader:
            filenum= num // 2000
            filename = csvfile.split('.')[0] + str(filenum) + ".csv"
            with open(filename, 'a', newline='') as fp2:
                writer = csv.writer(fp2)
                writer.writerow(line)
            num += 1
    return None

# 单线程试验
if __name__ == "__main__":
#    threads = []
    main('diffurl.csv')
    print('*'*45)
    print('*'*15 + "   ALL DONE!   " + '*'*15)
    print('*'*45)

#if __name__ == "__main__":
##    threads = []
#    for i in range(4):
#        t = threading.Thread(target=main, args=(f"landurls{i}.csv",))
#        t.start()
#    t.join()
#    print('*'*45)
#    print('*'*15 + "   ALL DONE!   " + '*'*15)
#    print('*'*45)

