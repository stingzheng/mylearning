# -*- coding: utf-8 -*-

import csv

header = ['name', 'gender', 'score']
f1 = ['hanmeimei', 'female', '100']
f2 = ['lilei', 'male', '99']

csv_file = open('csv_test.csv', 'w', newline='')
# 必须要设置newline=''，否则写入的时候会产生空行
writer = csv.writer(csv_file)

writer.writerow(header)
writer.writerow(f1)
writer.writerow(f2)

csv_file.close()

import json

json_data = {
        'results':[
                {
                        'location':{
                                'id':'asdfasdfsadf',
                                'name':'beijing',
                                'country':'chn',
                                'path':'tianjin-beijing',
                                'timezone':'asia'
                                }
                        }
                ]
        }

b = json.dumps(json_data)
print(b, type(b))

c = json.loads(b)
print(c, type(c))

with open('json_test.txt', 'w') as f:
    json.dump(json_data, f)

with open('json_test.txt', 'r') as f:
    d = json.load(f)
print(d)
