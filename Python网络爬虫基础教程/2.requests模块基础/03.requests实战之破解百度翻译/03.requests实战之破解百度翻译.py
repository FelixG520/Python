#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import json
if __name__ == "__main__":
    #1.指定url
    post_url='https://fanyi.baidu.com/sug'
    #2.进行UA伪装
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
    }
    #3.post请求参数处理（同get请求一致）
    #封装一个字典
    word=input('enter a word:')
    data={
        'kw':word
    }
    response = requests.post(url=post_url,data=data,headers=headers)

    #4.请求发送
    #5.获取响应数据:json()方法返回的是obj（如果确认响应数据是json类型的，才可以使用json（））
    dic_obj = response.json()
    #持久化存储
    fileName=word+'.json'
    fp=open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('Over!!!')


