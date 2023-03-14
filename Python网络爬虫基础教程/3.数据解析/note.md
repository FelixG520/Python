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

##### bs4实例

​	#1.实例化BeautifulSoup对象，需要将页面源码加载到该对象中

```python
url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
page_text = requests.get(url=url,headers=headers).text
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

#4.定位div标签的class属性值

![image-20230314104527743](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230314104527743.png)

```python
detail_soup = BeautifulSoup(detail_page_text,'lxml')
div_tag = detail_soup.find('div',class_='chapter_content')#定位div标签的class属性值
```

#5.获取div标签下的文本内容

```python
content = div_tag.text
fp.write(title + ':' + content + '\n')
```

完整代码

```python
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
    fp=open('./三国.txt',encoding='utf-8')
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
        print(title, '爬取成功！！！')

```

#### xpath解析

最常用且最便捷高效的一种解析方式。通用性。

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
    
    ```python
    #实例化好了一个etree对象，且将被解析的源码加载到了该对象中
    tree = etree.parse('test.html')
    r = tree.xpath('/html/head/title')#从head获取title,/表示从外层根结点
    print(r)#[<Element title at 0x1e8c335e3c0>]
    
    #返回的是element类型的对象，这个对象当中存储的是title标签下的文本内容
    ```
    
    - //:表示的是多个层级。可以表示从任意位置开始定位。
    
    ```python
    r = tree.xpath('/html/body/div')#body获取div标签
    r = tree.xpath('/html//div')
    r = tree.xpath('//div')
    #返回的结果一样
    
    r = tree.xpath('/html/body/div')#body获取div标签，有三组，返回的列表存储三个element类型对象
    #r = tree.xpath('/html//div')
    print(r) #[<Element div at 0x141c492df00>, <Element div at 0x141c492e2c0>, <Element div at 0x141c492e300>]
    ```
    
    
    - 属性定位：//div[@class='song'] tag[@attrName="attrValue"]
    
    ```python
    r = tree.xpath('//div[@class="song"]')
    print(r)  #[<Element div at 0x1d70e6fe3c0>]
    ```
    
    
    - 索引定位：//div[@class="song"]/p[3] 索引是从1开始的。
    
    ```python
    r = tree.xpath('//div[@class="song"]/p[3]')  # 苏轼所对应的p标签，第三个
    print(r)
    ```
    
    
    - 取文本：
        - /text() 获取的是标签中直系的文本内容
        - ![image-20230314120254131](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230314120254131.png)
    
        ```python
        r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')[0]
        print(r)#杜牧 -- 第5个li标签下的a标签
        ```
    
        - //text() 标签中非直系的文本内容（所有的文本内容）
    
          ![image-20230314120319907](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230314120319907.png)
    
        ```python
        r = tree.xpath('//li[7]//text()')
        print(r)#度蜜月 -- 第7个li标签的直系子标签当中
        r = tree.xpath('//div[@class="tang"]//text()')
        print(r)
        ```
    
    - 取属性：
        /@attrName     ==>img/src
    
    ```python
    r = tree.xpath('//div[@class="song"]/img/@src')
    print(r)#['http://www.baidu.com/meinv.jpg']
    ```

#### 需求：爬取58二手房中的房源信息

打开检查，发现所有的房源信息都在div标签中

![image-20230314164227814](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230314164227814.png)

而所有的div标签都在section中，section中有一个class属性值，因此先定位class属性值

```python
div_list=tree.xpath('//section[@class="list"]/div')
```

标题信息在div下的h3标签中，因此要在div中继续解析h3标签，h3标签在div下的a标签中的第二个div标签下的div中的div中

![image-20230314170221540](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230314170221540.png)

```python
for div in div_list:
    #div.xpath('div/div[2]/div/div/h3/text()')
    title = div.xpath('./div[2]/div/div/h3/text()')[0]
```

完整代码：

```python
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
```

#### 需求：解析下载图片数据

所有的图片都在li标签中，因此先先获取li标签

![image-20230314180615253](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230314180615253.png)

```python
    li_list=tree.xpath('//div[@class="slist"]/ul/li')
    for li in li_list:
        #属性定位：获取src属性值
        img_src = 'http://pic.netbian.com'+li.xpath('./a/img/@src')[0] #但并不是完整的地址，要补充添加
        img_name=li.xpath('./a/img/@alt')[0]+'.jpg'
        print(img_name,img_src)
```

完整代码：

```python
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
```

#### 案例-全国城市名称爬取

地区信息都在li标签下

![image-20230314185330297](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230314185330297.png)

完整代码：

```python
if __name__ == "__main__":
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url,headers=headers).text

    tree = etree.HTML(page_text)
    host_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    all_city_names = []
    #解析到了热门城市的城市名称
    for li in host_li_list:
        hot_city_name = li.xpath('./a/text()')[0]
        all_city_names.append(hot_city_name)

    #解析的是全部城市的名称
    city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    for li in city_names_list:
        city_name = li.xpath('./a/text()')[0]
        all_city_names.append(city_name)

    print(all_city_names,len(all_city_names))
```

优化，

```python
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
}
url = 'https://www.aqistudy.cn/historydata/'
page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
#解析到热门城市和所有城市对应的a标签
# div/ul/li/a -- //div[@class="bottom"]/ul/li/          热门城市a标签的层级关系
# div/ul/div[2]/li/a  -- //div[@class="bottom"]/ul/div[2]/li/a  全部城市a标签的层级关系
a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a') #|按位或
all_city_names = []
for a in a_list:
    city_name = a.xpath('./text()')[0]
    all_city_names.append(city_name)
print(all_city_names,len(all_city_names))
```



