# -*- coding: utf-8 -*-
'''
实现把每块地的txt文件转化成表格csv
'''
import csv
import os


def txt2csv(filepath, infilename, outfilename='landinfo.csv'):
    res = {}
    name = filepath + os.sep + infilename
    try:
        print(f"载入文件{name}")
        with open(name, 'r') as fp:
            for line in fp.readlines():
                key = line.strip().split("：")[0].strip().replace(u'\u3000', u'').replace(' ','')
                value = line.strip().split("：")[-1].strip().replace(u'\u3000', u'').replace(' ','')
                res.setdefault(key, value)
#        print(res)
        print(f"载入文件{name}------------------成功")
    except:
        print(f"载入文件{name}------------------失败")
        with open('txt2csvERR.log', 'a') as fp2:
            fp2.write(f"载入文件{name}------------------失败\n")
        return -1
    try:
        print(f"写入文件{infilename}")
        with open(outfilename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([res['地块编号'],res['具体位置'],res['出让面积'],res['容积率'],
                             res['用途'],res['供地方式'],res['使用年限'],res['竞得(人)'],
                             res['成交价格'],res['成交日期']])
        print(f"写入文件{infilename}------------------成功")
    except:
        print(f"写入文件{infilename}------------------失败")
        with open('txt2csvERR.log', 'a') as fp2:
            fp2.write(f"写入文件{infilename}------------------失败\n")
        return -2
    return 0


def main():
    filepath = ".\\landinfo"
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    for infilename in os.listdir(filepath):
        txt2csv(filepath, infilename, outfilename)


if __name__ == '__main__':
    outfilename = 'landinfo.csv'
    with open(outfilename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = ['地块编号', '具体位置', '出让面积', '容积率', '用途', '供地方式', '使用年限', '竞得(人)', '成交价格', '成交日期']
        writer.writerow(header)
    main()
    print('*'*45)
    print('*'*15 + "   ALL DONE!   " + '*'*15)
    print('*'*45)
