# -*- coding: utf-8 -*-
'''
网址为:http://www.tjlandmarket.com/notice/sell_notice/eed8a001717f40858fb5fff7e367e551/eaff75e4453d416a9ca53e8349627877/1.html
为了获取截止到目前的土地招拍挂的出让结果公告
每块地保存为一个txt
todo：后续再进行分析
'''
from selenium import webdriver
from time import sleep
import random
import csv
import os


# 构造地址池
landurls = []
url0 = "http://www.tjlandmarket.com/notice/sell_notice/eed8a001717f40858fb5fff7e367e551/eaff75e4453d416a9ca53e8349627877/"
for i in range(1, 406):
    landurls.append(f"{url0}{i}.html")

# 在landurl中获取每块地的页面,返回当前页面的url列表list
def getlandurl(url, dr):
    res = []
    dr.get(url)
    content = dr.find_elements_by_xpath("//ul[@class='fl']")[-1]
    rsc = content.find_elements_by_xpath(".//a[@href]")
    for i in rsc:
        res.append(i.get_attribute('href'))
        print(i.text,i.get_attribute('href'))
    return res

# 把列表写入csv
def writecsv(li, filename):
    with open(filename, 'a', newline='') as fp:
        writer = csv.writer(fp)
        for i in li:
            writer.writerow([i])
            print("写入", i)
    print("****************\n写入完毕！\n****************")
    return None



def main():
    global landurls
    dr = webdriver.Firefox()
    for i in landurls:
        print(f"当前页码{i.split('/')[-1]}")
        res = getlandurl(i, dr)
        # 暂停一下，缓冲缓冲
        for i in range(3):
            n = random.random()
            sleep(n)
            print(f'wait for {n} seconds')
        writecsv(res, 'landurls.csv')
    return "ALL DONE!"


if __name__=="__main__":
    main()

