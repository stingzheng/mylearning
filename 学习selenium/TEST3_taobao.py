# -*- coding: utf-8 -*-


from pyquery import PyQuery as pq
from selenium import webdriver

dr = webdriver.Firefox()

html = dr.page_source

pq_file = pq(html)

all_ = pq_file('#mainsrp-itemlist.items.item').items()




