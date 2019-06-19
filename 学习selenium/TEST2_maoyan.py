# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import csv


url_list = []
for i in range(10,11,10):
    url_list.append(f'http://maoyan.com/board/4?offset={i}')

# make csv frame
# 想要以文件名加后缀的办法创建csv文件，但是shell模式下无法获知文件名
# 在以文件模式运行的时候可以__file__,或者sys.argv[0],使用os.path.basename
csv_header = ['title', 'actors', 'score', 'introduce']
with open('maoyan.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csv_header)
#def writecsv(filename, value):
#    with open(filename, 'a') as fp:
#        reader = csv.reader(fp)
#        writer = csv.writer(fp)
#        writer.writerow(value)
#    return None

dr = webdriver.Firefox()
errlog = []

for url in url_list:
    value = []
    dr.get(url)
    time.sleep(1.5)
    try:
        for i in range(1,11):
            # get the title
            titlexpath = f'/html/body/div[4]/div/div/div[1]/dl/dd[{i}]/div/div/div[1]/p[1]/a'
            title = dr.find_element_by_xpath(titlexpath).get_attribute('title')
            # get the actors
            actorsxpath = f'/html/body/div[4]/div/div/div[1]/dl/dd[{i}]/div/div/div[1]/p[2]'
            actors = dr.find_element_by_xpath(actorsxpath).text
            # get the scores
            scorexpath1 = f'/html/body/div[4]/div/div/div[1]/dl/dd[{i}]/div/div/div[2]/p/i[1]'
            scorexpath2 = f'/html/body/div[4]/div/div/div[1]/dl/dd[{i}]/div/div/div[2]/p/i[2]'
            score = dr.find_element_by_xpath(scorexpath1).text + dr.find_element_by_xpath(scorexpath2).text
            # get the introduce
            dr.find_element_by_xpath(titlexpath).click()
            introxpath = '/html/body/div[4]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/span'
            time.sleep(1)
            intro = dr.find_element_by_xpath(introxpath).text
            dr.back()
            with open('maoyan.csv','a', newline='', errors='ignore') as f:
                writer = csv.writer(f)
                writer.writerow([title, actors, score, intro])
    # 这里有个片子的信息有错，提示编码错误，错误的双字节写入
    # TODO: 日后要解决编码错误的问题。
    # 处理办法（临时），在open参数里增加errors='ignore'，暂时解决了问题
    except:
        errlog.append(title)
        print(errlog)
        continue

dr.quit()








