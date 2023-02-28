#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import json
if __name__ == "__main__":
    #1.指定url
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    keyword=input('enter location:')
    page=input('enter page:')
    data = {
        'cname':'',
        'pid':'',
        'keyword': keyword,
        'pageIndex': page,
        'pageSize':'10',
    }
    #UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
    }
    #2.请求发送
    response = requests.post(url=url,data=data,headers=headers)
    #3.获取响应数据
    page_text = response.text
    #4.持久化存储
    filename=keyword+'KFC.html'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(filename,'over!!!')