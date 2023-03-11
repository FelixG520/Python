聚焦爬虫:爬取页面中指定的页面内容。
    - 编码流程：
        - 指定url
        - 发起请求
        - 获取响应数据
        - 数据解析
        - 持久化存储

### 数据解析分类：

- 正则

- bs4

- xpath（***）

数据解析原理概述：
    - 解析的局部的文本内容都会在标签之间或者标签对应的属性中进行存储
    1.进行指定标签的定位
    2.标签或者标签对应的属性中存储的数据值进行提取（解析）

#### 正则解析：

![image-20230303132115032](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230303132115032.png)

```python
ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
```

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
import os
#需求：爬取糗事百科中糗图板块下所有的糗图图片
if __name__ == "__main__":
    #创建一个文件夹，保存所有的图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')

    url = 'https://www.qiushibaike.com/pic/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

    }
    #使用通用爬虫对url对应的一整张页面进行爬取
    page_text = requests.get(url=url,headers=headers).text

    #使用聚焦爬虫将页面中所有的糗图进行解析/提取
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(ex,page_text,re.S)
    # print(img_src_list)
    for src in img_src_list:
        #拼接出一个完整的图片url
        src = 'https:'+src
        #请求到了图片的二进制数据
        img_data = requests.get(url=src,headers=headers).content
        #生成图片名称
        img_name = src.split('/')[-1]
        #图片存储的路径
        imgPath = './qiutuLibs/'+img_name
        with open(imgPath,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功！！！')
```

多页解析：

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
import os
#需求：爬取糗事百科中糗图板块下所有的糗图图片
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

    }
    #创建一个文件夹，保存所有的图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')
    #设置一个通用的url模板
    url = 'https://www.qiushibaike.com/pic/page/%d/?s=5184961'
    # pageNum = 2

    for pageNum in range(1,36):
        #对应页码的url
        new_url = format(url%pageNum)#返回字符串


        #使用通用爬虫对url对应的一整张页面进行爬取
        page_text = requests.get(url=new_url,headers=headers).text

        #使用聚焦爬虫将页面中所有的糗图进行解析/提取
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex,page_text,re.S)
        # print(img_src_list)
        for src in img_src_list:
            #拼接出一个完整的图片url
            src = 'https:'+src
            #请求到了图片的二进制数据
            img_data = requests.get(url=src,headers=headers).content
            #生成图片名称
            img_name = src.split('/')[-1]
            #图片存储的路径
            imgPath = './qiutuLibs/'+img_name
            with open(imgPath,'wb') as fp:
                fp.write(img_data)
                print(img_name,'下载成功！！！')



```

#### bs4进行数据解析

- 数据解析的原理：
    - 1.标签定位
    - 2.提取标签、标签属性中存储的数据值
    - bs4数据解析的原理：
    - 1.实例化一个BeautifulSoup对象，并且将页面源码数据加载到该对象中
    - 2.通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取

    - 环境安装：
    - #pip install lxml -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

```python
pip install bs4
pip install lxml
```

   - 如何实例化BeautifulSoup对象：

```python
from bs4 import BeautifulSoup
```

- 对象的实例化：
    - 1.将本地的html文档中的数据加载到该对象中 -- BeautifulSoup对象

    ```python
    fp = open('./test.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    ```

    - 2.将互联网上获取的页面源码加载到该对象中 --<font color='red'> 常用</font>

    ```python
    page_text = response.text
    soup = BeatifulSoup(page_text,'lxml')
    ```

- 提供的用于数据解析的<font color='red'>方法和属性</font>：
    - soup.tagName:返回的是文档中第一次出现的tagName对应的标签

      ```
      print(soup.a) #打印第一次出现的a标签
      ```

      ![image-20230306134945399](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230306134945399.png)

      ```python
      print(soup.div) #打印第一次出现的div标签
      ```

      ![image-20230306135143393](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230306135143393.png)

    - soup.find():

      - soup.find('tagName'):等同于soup.div

        ```python
        print(soup.find('div'))  #相当于print(soup.div)
        ```
      
      ![image-20230307105221118](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230307105221118.png)

      -  属性定位：class_/id/attr等属性
      
        ```python
        soup.find('div',class='song') #找到属性为song的div
        ```
      
        ![image-20230307105849231](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230307105849231.png)
      
      - 返回符合要求的所有标签（列表）-- soup.find_all('tagName')
      
        ```python
        print(soup.find_all('a'))  #找到所有的a标签
        ```
      
        ![image-20230307110202924](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230307110202924.png)

- select：

    - select('<font color='red'>某种选择器</font>（id，class，标签...选择器）'),返回的是一个<font color='red'>列表</font>。

    ```python
    print(soup.select('.tang'))
    ```

    ![image-20230307110448512](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230307110448512.png)

    - 层级选择器：返回值是个列表

      - soup.select('.tang > ul > li > a')：>表示的是一个层级

      ![image-20230307110836883](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230307110836883.png)

      ```python
      print(soup.select('.tang > ul > li > a'))
      ```

      ![image-20230307111059078](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230307111059078.png)

      - 查看第一个标签，即列表的第一个元素

      ```python
      print(soup.select('.tang > ul > li > a')[0])
      ```

      ![image-20230307111250853](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230307111250853.png)

      - oup.select('.tang > ul a')：空格表示的多个层级

      ```python
      print(soup.select('.tang > ul a')[0])
      ```

      ![image-20230307111453346](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230307111453346.png)

- 获取标签之间的文本数据：

    - soup.a.text/string/get_text()

    - text/get_text():可以获取某一个标签中所有的文本内容

      ```python
      print(soup.select('.tang > ul a')[0].text) #获得该标签下的文本内容
      print(soup.select('.tang > ul a')[0].get_text())
      ```

      ![image-20230307112502355](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230307112502355.png)

      ```python
      print(soup.find('div',class_='song').text)
      ```

      ![image-20230307112845415](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230307112845415.png)

    - string：只可以获取该标签下面直系的文本内容

      ![image-20230307113017973](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230307113017973.png)

      song标签下没有直系的文本内容，因此返回值为None

      ```python
      print(soup.find('div',class_='song').string)
      ```

      ![image-20230307113120691](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230307113120691.png)

- 获取标签中属性值：soup.a['href']

  ![image-20230307113519271](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230307113519271.png)

  ```python
  print(soup.select('.tang > ul a')[0]['href'])
  ```

  ![image-20230307113324404](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230307113324404.png)

#### bs4实例

​	#1.实例化BeautifulSoup对象，需要将页面源码加载到该对象中

```python
url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
page_text = requests.get(url=url)
soup = BeautifulSoup(page_text,'lxml')
```

#2.解析章节标题和详情页的url

![image-20230307115230190](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230307115230190.png)

```python
li_list = soup.select('.book-mulu > ul > li')
```

#3.获取li标签中的a标签

```python
for li in li_list:
	title = li.a.string  #章节标题是直系文本
	detail_url = 'https://www.shicimingju.com' + li.a['href'] #获取属性值，不完整要拼接
```

xpath解析：最常用且最便捷高效的一种解析方式。通用性。

    - xpath解析原理：
        - 1.实例化一个etree的对象，且需要将被解析的页面源码数据加载到该对象中。
        - 2.调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获。
    - 环境的安装：
        - pip install lxml
    - 如何实例化一个etree对象:from lxml import etree
        - 1.将本地的html文档中的源码数据加载到etree对象中：
            etree.parse(filePath)
        - 2.可以将从互联网上获取的源码数据加载到该对象中
            etree.HTML('page_text')
        - xpath('xpath表达式')
    - xpath表达式:
        - /:表示的是从根节点开始定位。表示的是一个层级。
        - //:表示的是多个层级。可以表示从任意位置开始定位。
        - 属性定位：//div[@class='song'] tag[@attrName="attrValue"]
        - 索引定位：//div[@class="song"]/p[3] 索引是从1开始的。
        - 取文本：
            - /text() 获取的是标签中直系的文本内容
            - //text() 标签中非直系的文本内容（所有的文本内容）
        - 取属性：
            /@attrName     ==>img/src

作业：
    爬取站长素材中免费简历模板


        ，





