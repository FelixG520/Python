# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

#urllib爬虫常用
#按住ctrl左键urllib，跳到__init__.py的文件当中，说明urllib是一个包，因为包里有__init__.py文件；包里含有多种模块


import urllib.request   #request是发送请求的意思
print(urllib.request.urlopen('http://www.baidu.com').read())  #将百度返回的东西全部读取

