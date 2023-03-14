#!/usr/bin/env python
# -*- coding:utf-8 -*-
from lxml import etree
if __name__ == "__main__":
    #实例化好了一个etree对象，且将被解析的源码加载到了该对象中
    tree = etree.parse('test.html')
    # r = tree.xpath('/html/head/title')#从head获取title,/表示从外层根结点定位
    # print(r)  #[<Element title at 0x1e8c335e3c0>]

    # r = tree.xpath('/html/body/div')#body获取div标签，有三组，返回的列表存储三个element类型对象
    # print(r) #[<Element div at 0x141c492df00>, <Element div at 0x141c492e2c0>, <Element div at 0x141c492e300>]
    # r = tree.xpath('/html//div')
    # print(r) #[<Element div at 0x141c492df00>, <Element div at 0x141c492e2c0>, <Element div at 0x141c492e300>]
    # r = tree.xpath('//div')
    # print(r)

    #属性定位
    # r = tree.xpath('//div[@class="song"]')
    # print(r)
    # r = tree.xpath('//div[@class="song"]')#苏轼所对应的p标签，第三个
    # print(r)

    #索引定位
    # r = tree.xpath('//div[@class="song"]/p[3]')  # 苏轼所对应的p标签，第三个
    # print(r)
    # r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')[0] #列表中只有一个元素，list[0]
    # print(r)#杜牧 -- 第5个li标签下的a标签
    # r = tree.xpath('//li[7]//text()')
    # print(r)#度蜜月 -- 第7个li标签的直系子标签当中
    # r = tree.xpath('//div[@class="tang"]//text()')
    # print(r)
    r = tree.xpath('//div[@class="song"]/img/@src')
    print(r)#['http://www.baidu.com/meinv.jpg']

