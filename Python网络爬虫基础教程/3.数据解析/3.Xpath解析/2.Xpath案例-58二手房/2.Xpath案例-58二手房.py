#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from lxml import etree

#需求：爬取58二手房中的房源信息
if __name__ == "__main__":
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
    }
    url='https://bj.58.com/ershoufang/'
    page_text=requests.get(url=url,headers=headers).text

    #数据解析
    tree=etree.HTML(page_text) #实例化etree对象
    #属性定位，存储的div标签对象
    div_list=tree.xpath('//section[@class="list"]/div')
    #从每一个列表元素所表示的div标签当中再将h3标签解析出来
    fp=open('./58.txt','w',encoding='utf-8')
    for div in div_list:
        # title = div.xpath('div/div[2]/div/div/h3/text()')
        title = div.xpath('./a/div[2]/div/div/h3/text()')[0]
        print(title)
        fp.write(title+'\n')


