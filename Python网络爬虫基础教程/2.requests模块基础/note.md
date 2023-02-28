#### requests模块

​    - urllib模块
​    - requests模块

requests模块：python中原生的一款基于网络请求的模块，功能非常强大，简单便捷，效率极高。
<font color='red'>作用：模拟浏览器发请求。</font>

##### 如何使用：（requests模块的编码流程）

​    - 指定url
​        - UA伪装
​        - 请求参数的处理
​    - 发起请求
​    - 获取响应数据
​    - 持久化存储

##### 环境安装：

​    pip install requests

##### 实战编码：

​    - 需求：爬取搜狗首页的页面数据

```python
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#- 需求：爬取搜狗首页的页面数据
import requests
if __name__ == "__main__":
    #1.指定url
    url='https://www.sogou.com/'
    #2.发起请求
    #get方法会返回一个响应对象
    response = requests.get(url=url)
    #3.获取响应数据，text字符串形式的响应数据
    page_text = response.text
    #4.持久化存储
    with open('sougou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束！！！')
```

##### 实战巩固

需求：爬取搜狗指定词条对应的搜索结果页面（简易网页采集器）
​        - UA检测
​        - UA伪装

```python
#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#UA：User-Agent（请求载体的身份标识）
#UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器，
#说明该请求是一个正常的请求。但是，如果检测到请求的载体身份标识不是基于某一款浏览器的，则表示该请求
#为不正常的请求（爬虫），则服务器端就很有可能拒绝该次请求。

#UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
import requests
if __name__ == "__main__":
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
    }
    # 1.指定url
    #url='https://cn.bing.com/search?q=西安明德理工学院'
    url = 'https://cn.bing.com/search?'
    #处理url携带的参数：封装到字典中
    kw=input('enter a word:')
    param={
        'q':kw   #字典创建成功
    }

    #2.发起请求
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,params=param,headers=headers)#将字典赋值给params参数

    #3.获取响应数据
    page_text=response.text
    fileName=kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功！！！')
```

需求：破解百度翻译
​    - post请求（携带了参数）
​    - 响应数据是一组json数据

```python
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



```

需求：爬取豆瓣电影分类排行榜 https://movie.douban.com/中的电影详情数据

```python
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import json
if __name__ == "__main__":
    #url = 'https://movie.douban.com/j/chart/top_list?type=19&interval_id=100%3A90&action=&start=20&limit=20'
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '19',
        'interval_id': '100:90',
        'action':'',
        'start': '0', #从库中的第几部电影去取
        'limit': '20',#一次取出的个数
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
    }
    response = requests.get(url=url,params=param,headers=headers)

    list_data = response.json()

    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    print('over!!!')
```

作业：爬取肯德基餐厅查询http://www.kfc.com.cn/kfccda/index.aspx中指定地点的餐厅数据

```python
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
        'pageSize':10,
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
```

- 需求：爬取国家药品监督管理总局中基于中华人民共和国化妆品生产许可证相关数据
            http://125.35.6.84:81/xk/

        - 动态加载数据
        - 首页中对应的企业信息数据是通过ajax动态请求到的。
    
        http://125.35.6.84:81/xk/itownet/portal/dzpz.jsp?id=e6c1aa332b274282b04659a6ea30430a
        http://125.35.6.84:81/xk/itownet/portal/dzpz.jsp?id=f63f61fe04684c46a016a45eac8754fe
        - 通过对详情页url的观察发现：
            - url的域名都是一样的，只有携带的参数（id）不一样
            - id值可以从首页对应的ajax请求到的json串中获取
            - 域名和id值拼接处一个完整的企业对应的详情页的url
        - 详情页的企业详情数据也是动态加载出来的
            - http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById
            - http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById
            - 观察后发现：
                - 所有的post请求的url都是一样的，只有参数id值是不同。
                - 如果我们可以批量获取多家企业的id后，就可以将id和url形成一个完整的详情页对应详情数据的ajax请求的url

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import  requests
import json
if __name__ == "__main__":

    #批量获取不同企业的id值 -- url都相同
    url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    #参数的封装
    for page in range(1,6):
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName':'',
            'conditionType': '1',
            'applyname':'',
            'applysn':'',
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
        }
        id_list=[] #存储企业ID
        all_data_list = [] #存储所有企业详情数据
        json_ids = requests.post(url=url,headers=headers,data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
    #获取企业详情数据
    post_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id':id
        }
        detail_json = requests.post(url=post_url,headers=headers,data=data).json()
        # print(detail_json,'-------------ending-----------')
        all_data_list.append(detail_json)

    #持久化存储all_data_list
    fp = open('./allData.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    print('over!!!')
```

###### 数据解析：

​    聚焦爬虫
​    正则
​    bs4
​    xpath