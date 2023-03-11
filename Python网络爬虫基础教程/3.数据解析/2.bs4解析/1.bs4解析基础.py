#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
if __name__ == "__main__":
    #将本地的html文档中的数据加载到该对象中
    fp = open('./test.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    #print(soup)

    #相关的属性和方法
    #soup.tagName 返回的是html中第一次出现的tagName标签
    #print(soup.a) #打印第一次出现的a标签
    #print(soup.div) #打印第一次出现的div标签
    #find('tagName'):等同于soup.div
    #print(soup.find('div'))  #print(soup.div)

    print(soup.find('div',class_='song')) #找到属性为song的div
    # print(soup.find_all('a'))  #找到所有的a标签
    # print(soup.select('.tang'))
    # print(soup.select('.tang > ul > li > a')[0]) #查看第一个标签，即列表的第一个元素
    # print(soup.select('.tang > ul a')[0])
    # print(soup.select('.tang > ul a')[0].text) #获得该标签下的文本内容
    # print(soup.select('.tang > ul a')[0].get_text())
    # print(soup.find('div',class_='song').text)
    # print(soup.find('div',class_='song').string)
    # print(soup.select('.tang > ul a')[0]['href'])

