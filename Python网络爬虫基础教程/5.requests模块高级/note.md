模拟登录：
- 爬取基于某些用户的用户信息。
  需求：对人人网进行模拟登录。

- 点击登录按钮之后会发起一个post请求

- post请求中会携带登录之前录入的相关的登录信息（用户名，密码，验证码......）

- 验证码：每次请求都会变化

  ```python
  #编码流程：
  #1.验证码的识别，获取验证码图片的文字数据
  #2.对post请求进行发送（处理请求参数）
  #3.对响应数据进行持久化存储
  
  from CodeClass import YDMHttp #当前目录下的CodeClass类的函数
  import requests
  from lxml import etree
  #封装识别验证码图片的函数
  def getCodeText(imgPath,codeType):
      # 普通用户用户名
      username = 'bobo328410948'
  
      # 普通用户密码
      password = 'bobo328410948'
  
      # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
      appid = 6003
  
      # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
      appkey = '1f4b564483ae5c907a1d34f8e2f2776c'
  
      # 图片文件：即将被识别的验证码图片的路径
      filename = imgPath
  
      # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
      codetype = codeType
  
      # 超时时间，秒
      timeout = 20
      result = None
      # 检查
      if (username == 'username'):
          print('请设置好相关参数再测试')
      else:
          # 初始化
          yundama = YDMHttp(username, password, appid, appkey)
  
          # 登陆云打码
          uid = yundama.login();
          print('uid: %s' % uid)
  
          # 查询余额
          balance = yundama.balance();
          print('balance: %s' % balance)
  
          # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
          cid, result = yundama.decode(filename, codetype, timeout);
          print('cid: %s, result: %s' % (cid, result))
      return result
  
  
  #1.对验证码图片进行捕获和识别
  headers = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
  }
  url = 'http://www.renren.com/SysHome.do'
  page_text = requests.get(url=url,headers=headers).text
  tree = etree.HTML(page_text)
  code_img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
  code_img_data = requests.get(url=code_img_src,headers=headers).content
  with open('code.jpg', 'wb') as fp:#将验证码图片保存到本地
      fp.write(code_img_data)
  
  #使用云打码提供的示例代码对验证码图片进行识别
  result = getCodeText('code.jpg',1000)
  print(result) #打印输出识别的验证码
  #post请求的发送（模拟登录）
  login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019431046983'
  data = {
      'email': 'www.zhangbowudi@qq.com',
      'icode': result, #验证码
      'origURL': 'http://www.renren.com/home',
      'domain': 'renren.com',
      'key_id': '1',
      'captcha_type': 'web_login',
      'password': '06768edabba49f5f6b762240b311ae5bfa4bcce70627231dd1f08b9c7c6f4375',
      'rkey': '1028219f2897941c98abdc0839a729df',
      'f':'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dgds6TUs9Q1ojOatGda5mVsLKC34AYwc5XiN8OuImHRK%26wd%3D%26eqid%3D8e38ba9300429d7d000000035cedf53a',
  }
  response = requests.post(url=login_url,headers=headers,data=data)
  print(response.status_code)
  
  login_page_text=response.text
  with open('renren.html','w',encoding='utf-8') as fp:
      fp.write(login_page_text)
  ```

  

需求：爬取当前用户的相关的用户信息（个人主页中显示的用户信息）

http/https协议特性：无状态。
没有请求到对应页面数据的原因：
    发起的第二次基于个人主页页面请求的时候，服务器端并不知道该此请求是基于登录状态下的请求。
cookie：用来让服务器端记录客户端的相关状态。

- 手动处理：通过抓包工具获取cookie值，将该值封装到headers中。（不建议）

     ```python
     #手动cookie处理
     # headers = {
     #     'Cookie':'xxxx'
     # }
     ```

- 自动处理：

     - cookie值的来源是哪里？
         - 模拟登录post请求后，由服务器端创建。

     - session会话对象：

       - 作用：

       - 1.可以进行请求的发送。

       - 2.如果请求过程中产生了cookie，则该cookie会被自动存储/携带在该session对象中。

     - 创建一个session对象：session = requests.Session()

     - 使用session对象进行模拟登录post请求的发送（cookie就会被存储在session中）

     - session对象对个人主页对应的get请求进行发送（携带了cookie）

```python
#使用session进行post请求的发送
response = session.post(url=login_url,headers=headers,data=data)
print(response.status_code)

#爬取当前用户的个人主页对应的页面数据
detail_url = 'http://www.renren.com/289676607/profile'
#手动cookie处理
# headers = {
#     'Cookie':'xxxx'
# }
#使用携带cookie的session进行get请求的发送
detail_page_text = session.get(url=detail_url,headers=headers).text
with open('../bobo.html', 'w', encoding='utf-8') as fp:
    fp.write(detail_page_text)
```

代理：破解封IP这种反爬机制。
什么是代理：
    - 代理服务器。
代理的作用：
    - 突破自身IP访问的限制。
    - 隐藏自身真实IP
代理相关的网站：
    - 快代理
    - 西祠代理
    - www.goubanjia.com
代理ip的类型：
    - http：应用到http协议对应的url中
    - https：应用到https协议对应的url中

代理ip的匿名度：
    	- 透明：服务器知道该次请求使用了代理，也知道请求对应的真实ip
        - 匿名：知道使用了代理，不知道真实ip
        - 高匿：不知道使用了代理，更不知道真实的ip