#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

#需求：爬取三国演义小说所有的章节标题和章节内容http://www.shicimingju.com/book/sanguoyanyi.html
if __name__ == "__main__":
    #对首页的页面数据进行爬取
    headers={
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
    }
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url,headers=headers).text
    #需要在首页中解析章节的标题和详情页的url（bs4）
    #1.实例化BeautifulSoup对象，需要将页面源码加载到该对象中
    soup = BeautifulSoup(page_text,'lxml')
    #2.解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul > li')
    fp=open('./三国.txt','w',encoding='ISO-8859-1')
    #3.获取li标签中的a标签
    for li in li_list:
        title = li.a.string  #章节标题是直系文本
        detail_url = 'https://www.shicimingju.com' + li.a['href'] #获取属性值，不完整要拼接
        #对详情页发起请求，解析出章节内容
        detail_page_text=requests.get(url=detail_url,headers=headers).text
        #解析出详情页中的章节内容
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_='chapter_content')#定位div标签的class属性值
        # 解析到了章节的内容
        content = div_tag.text
        fp.write(title + ':' + content + '\n')
        #title = title.encode('iso-8859-1').decode('gbk')
        print(title, '爬取成功！！！')


