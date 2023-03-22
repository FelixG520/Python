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
  
- 3.单线程+异步协程（推荐）：
    	event_loop：事件循环，相当于一个无限循环，我们可以把一些函数注册到这个事件循环上，当满足某些条件的时候，函数就会被循环执行。

    coroutine：协程对象，我们可以将协程对象注册到事件循环中，它会被事件循环调用。
    我们可以使用 async 关键字来定义一个方法，这个方法在调用时不会立即被执行，而是返回
    一个协程对象。

    task：任务，它是对协程对象的进一步封装，包含了任务的各个状态。

    future：代表将来执行或还没有执行的任务，实际上和 task 没有本质区别。

    async 定义一个协程.

    await 用来挂起阻塞方法的执行。



