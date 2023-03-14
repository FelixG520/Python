#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#需求：解析下载图片数据 http://pic.netbian.com/4kmeinv/
import requests
from lxml import etree
import os
if __name__ == "__main__":
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
    }
    url = 'http://pic.netbian.com/4kmeinv/'
    response=requests.get(url=url,headers=headers) #先获取响应对象
    #解决乱码问题 -- 原因是网页编码方式和代码编码不同，修改网页编码即可
    #response.encoding = 'utf-8'
    page_text=response.text

    #数据解析：src的属性值  alt属性
    tree=etree.HTML(page_text)
    #获取li标签列表
    li_list=tree.xpath('//div[@class="slist"]/ul/li')
    #创建文件夹保存图片
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    for li in li_list:
        #属性定位：获取src属性值
        img_src = 'http://pic.netbian.com'+li.xpath('./a/img/@src')[0] #但并不是完整的地址，要补充添加
        img_name=li.xpath('./a/img/@alt')[0]+'.jpg'
        #如果上面的编码改完还是乱码 -- 通用处理中文乱码的解决方案
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        print(img_name,img_src)

        #持久化存储
        img_date = requests.get(url=img_src,headers=headers).content
        #指定图片下载路径
        img_path = './picLibs/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_date)
            print(img_name,"下载成功！！！")



