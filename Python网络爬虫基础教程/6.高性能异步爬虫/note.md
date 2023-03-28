同步爬虫，爬取多个网页过于缓慢，要等阻塞操作结束才能继续往下执行

```python
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
}
urls = [
    'http://xmdx.sc.chinaz.net/Files/DownLoad/jianli/201904/jianli10231.rar',
    'http://zjlt.sc.chinaz.net/Files/DownLoad/jianli/201904/jianli10229.rar',
    'http://xmdx.sc.chinaz.net/Files/DownLoad/jianli/201904/jianli10231.rar'
]

#获取服务器端响应数据
def get_content(url):
    print('正在爬取：',url)
    #get方法是一个阻塞的方法
    response = requests.get(url=url,headers=headers)
    if response.status_code == 200 :#响应成功
        return response.content

#数据解析
def parse_content(content):
    print('响应数据的长度为：',len(content))


for url in urls:
    content = get_content(url)
    parse_content(content)
```

高性能异步爬虫
目的：在爬虫中使用异步实现高性能的数据爬取操作。

异步爬虫的方式：
- 1.多线程，多进程（不建议）：
     	好处：可以为相关阻塞的操作单独开启线程或者进程，阻塞操作就可以异步执行。
     	弊端：无法无限制的开启多线程或者多进程。

- 2.线程池、进程池（适当的使用）：
  	好处：我们可以降低系统对进程或者线程创建和销毁的一个频率，从而很好的降低系统的开销。
  	弊端：池中线程或进程的数量是有上限。

  - 使用单线程串行方式执行
  
  
  ```python
  import time
  #使用单线程串行方式执行
  def get_page(str):
      print("正在下载 ：",str)
      time.sleep(2)
      print('下载成功：',str)
  
  name_list =['xiaozi','aa','bb','cc']
  
  start_time = time.time()
  
  for i in range(len(name_list)):
      get_page(name_list[i])
  
  end_time = time.time()
  print('%d second'% (end_time-start_time))
  ```
  
  耗时8s
  
  ![image-20230322114936751](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230322114936751.png)
  
  - 使用线程池串行方式执行
  
    ```python
    import time
    #导入线程池模块对应的类
    from multiprocessing.dummy import Pool
    #使用线程池方式执行
    start_time = time.time()
    def get_page(str):
        print("正在下载 ：",str)
        time.sleep(2)
        print('下载成功：',str)
    
    name_list =['xiaozi','aa','bb','cc']
    
    #实例化一个线程池对象
    pool = Pool(4)
    #将列表中每一个列表元素传递给get_page进行处理。
    pool.map(get_page,name_list)
    pool.close()
    pool.join()
    end_time = time.time()
    print(end_time-start_time)
    ```
    
    ![image-20230328104956580](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230328104956580.png)



原则：线程池处理的是阻塞且较为耗时的操作

案例：需求：爬取梨视频的视频数据

```python
import requests
from lxml import etree
import random
import os
from multiprocessing.dummy import Pool

if __name__ == '__main__':
    # 生成一个存视频的文件夹
    if not os.path.exists('./video'):
        os.mkdir('./video')

    url = 'https://www.pearvideo.com/category_5'
    headers = {
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54"
    }
    # proxies={'https': '62.210.38.37:3838'} 代理ip，用了太慢
    response = requests.get(url=url, headers=headers)
    page_text = response.text

    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="listvideoListUl"]/li')

    urls = []  # 储存所有视频的连接和名字
    for li in li_list:
        new_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
        new_name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
        # 这个方法行不通。因为mp4是动态加载出来的，因此需要抓包ajax请求中的url，不知道怎么用python抓包，用浏览器的抓包工具
        new_page_text = requests.get(url=new_url, headers=headers).text
        new_tree = etree.HTML(new_page_text)
        name = new_tree.xpath('//*[@id="detailsbd"]/div[1]/div[2]/div/div[1]/h1/text()')[0]
        # print(name)

        # 通过抓包ajax得到一个可以发送的url和请求伪装的视频的url，
        id_ = str(li.xpath('./div/a/@href')[0]).split('_')[1]
        # 可发送请求的url
        ajax_url = 'https://www.pearvideo.com/videoStatus.jsp?'
        params = {
            'contId': id_,
            'mrd': str(random.random())
        }
        ajax_headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54',
            'Referer': 'https://www.pearvideo.com/video_' + id_
        }
        # 加了'Referer': 'https://www.pearvideo.com/video_1708144'后就不会显示该视频已下架了
        dic_obj = requests.get(url=ajax_url, params=params, headers=ajax_headers).json()
        video_url = dic_obj["videoInfo"]['videos']["srcUrl"]

        # 此处视频地址做了加密即ajax中得到的地址需要加上cont-,并且修改一段数字为id才是真地址
        # 真地址："https://video.pearvideo.com/mp4/third/20201120/cont-1708144-10305425-222728-hd.mp4"
        # 伪地址："https://video.pearvideo.com/mp4/third/20201120/1606132035863-10305425-222728-hd.mp4"

        # 得到真url,做字符串处理
        video_true_url = ''
        s_list = str(video_url).split('/')
        # print(s_list)
        for i in range(0, len(s_list)):
            if i < len(s_list) - 1:
                video_true_url += s_list[i] + '/'
            else:
                ss_list = s_list[i].split('-')
                # print(ss_list)
                for j in range(0, len(ss_list)):
                    if j == 0:
                        video_true_url += 'cont-' + id_ + '-'
                    elif j == len(ss_list) - 1:
                        video_true_url += ss_list[j]
                    else:
                        video_true_url += ss_list[j] + '-'
        # print(video_true_url)

        dic = {
            'name': name,
            'url': video_true_url
        }
        urls.append(dic)

    # 使用线程池对视频数据进行请求(较为耗时的阻塞操作)
    def get_video_data(dic_):
        url_ = dic_['url']
        print(dic_['name'], '正在下载.....')
        video_data = requests.get(url=url_, headers=headers).content
        video_path = './video/' + dic_['name']
        with open(video_path, 'wb') as fp:
            fp.write(video_data)
            print(dic_['name'], '下载成功!!!!!')


    pool = Pool(4)
    pool.map(get_video_data, urls)

    pool.close()
    pool.join()

```

- 3.单线程+异步协程（推荐）：

event_loop：事件循环，相当于一个无限循环，我们可以把一些函数注册到这个事件循环上，当满足某些条件的时候，函数就会被循环执行。

```python
import asyncio

async def request(url):
    print('正在请求的url是',url)
    print('请求成功,',url)
    return url
#async修饰的函数，调用之后返回的一个协程对象
c = request('www.baidu.com')

#创建一个事件循环对象
loop = asyncio.get_event_loop()

#将协程对象注册到loop中，然后启动loop
loop.run_until_complete(c)
```

coroutine：协程对象，我们可以将协程对象注册到事件循环中，它会被事件循环调用。
我们可以使用 async 关键字来定义一个方法，这个方法在调用时不会立即被执行，而是返回
一个协程对象。

task：任务，它是对协程对象的进一步封装，包含了任务的各个状态。

```python
loop = asyncio.get_event_loop()
#基于loop创建了一个task对象
task = loop.create_task(c)
print(task)

loop.run_until_complete(task)

print(task)
```

future：代表将来执行或还没有执行的任务，实际上和 task 没有本质区别。

```python
#future的使用
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
print(task)
loop.run_until_complete(task)
print(task)
```

async 定义一个协程.

await 用来挂起阻塞方法的执行。

多任务异步携程

```python
import asyncio
import time

async def request(url):
    print('正在下载',url)
    #在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步。
    # time.sleep(2)
    #当在asyncio中遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)
    print('下载完毕',url)

start = time.time()
urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.goubanjia.com'
]

#任务列表：存放多个任务对象
stasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)

loop = asyncio.get_event_loop()
#需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stasks))

print(time.time()-start)
```

aiohttp实现多任务异步协程

```python
#环境安装：pip install aiohttp
#使用该模块中的ClientSession
import requests
import asyncio
import time
import aiohttp

start = time.time()
# urls = [
#     'http://127.0.0.1:5000/bobo','http://127.0.0.1:5000/jay','http://127.0.0.1:5000/tom',
#     'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/jay', 'http://127.0.0.1:5000/tom',
#     'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/jay', 'http://127.0.0.1:5000/tom',
#     'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/jay', 'http://127.0.0.1:5000/tom',
#
# ]
from multiprocessing.dummy import Pool
pool = Pool(2)

urls = []
for i in range(10):
    urls.append('http://127.0.0.1:5000/bobo')
print(urls)
async def get_page(url):
    async with aiohttp.ClientSession() as session:
        #get()、post():
        #headers,params/data,proxy='http://ip:port'
        async with await session.get(url) as response:
            #text()返回字符串形式的响应数据
            #read()返回的二进制形式的响应数据
            #json()返回的就是json对象
            #注意：获取响应数据操作之前一定要使用await进行手动挂起
            page_text = await response.text()
            print(page_text)
            
tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print('总耗时:',end-start)
```

selenium模块的基本使用

便捷的获取网站中动态加载的数据 
