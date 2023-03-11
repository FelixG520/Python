#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

#需求：爬取三国演义小说所有的章节标题和章节内容http://www.shicimingju.com/book/sanguoyanyi.html
if __name__ == "__main__":
    #对首页的页面数据进行爬取
    headers={
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
    }
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url)
    #需要在首页中解析章节的标题和详情页的url（bs4）
    #1.实例化BeautifulSoup对象，需要将页面源码加载到该对象中
    soup = BeautifulSoup(page_text,'lxml')
    #2.解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul > li')
    #3.获取li标签中的a标签
    for li in li_list:
        title = li.a.string  #章节标题是直系文本
        detail_url = 'https://www.shicimingju.com' + li.a['href'] #获取属性值，不完整要拼接
        #对详情页发起请求，解析出章节内容
        detail_page_text=requests.get(url=detail_url,headers=headers).text
        #解析出详情页中的章节内容


