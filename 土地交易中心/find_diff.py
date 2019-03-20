# -*- coding: utf-8 -*-


from selenium import webdriver
from time import sleep
import random
import csv


# 构造地址池
landurls = []
url0 = "http://www.tjlandmarket.com/notice/sell_notice/eed8a001717f40858fb5fff7e367e551/eaff75e4453d416a9ca53e8349627877/"
for i in range(1, 406):
    landurls.append(f"{url0}{i}.html")


def csv2set(csvfile=".\\csv_file\\landinfo.csv"):
    res = []
    with open(csvfile, 'r') as fp:
        reader = csv.reader(fp)
        for line in reader:
            res.append(line[0])
        res = set(res)
    return res

nameset = csv2set()

# 在landurl中获取每块地的页面,返回当前页面的url列表list
def getdifflandurl(url, dr):
    global nameset
    res = {}
    dr.get(url)
    content = dr.find_elements_by_xpath("//ul[@class='fl']")[-1]
    rsc = content.find_elements_by_xpath(".//a[@href]")
    for i in rsc:
        if i.text.replace('•','').strip() not in nameset:
            res[i.text.replace('•','').strip()] = i.get_attribute('href')
            print(i.text,i.get_attribute('href'))
        else:
            continue
    return res


# 把列表写入csv
def writediffcsv(res, filename="diffurl.csv"):
    with open(filename, 'a', newline='', encoding='utf-8') as fp:
        writer = csv.writer(fp)
        for key, value in res.items():
            writer.writerow([key, value])
            print("写入", i)
    print("****************\n写入完毕！\n****************")
    return None

def main():
    global landurls
    dr = webdriver.Firefox()
    for i in landurls:
        print(f"当前页码{i.split('/')[-1]}")
        res = getdifflandurl(i, dr)
        # 暂停一下，缓冲缓冲
        for i in range(2):
            n = random.random()
            sleep(n)
            print(f'wait for {n} seconds')
        writediffcsv(res, 'diffurl.csv')
    return "ALL DONE!"

if __name__=="__main__":
    main()

