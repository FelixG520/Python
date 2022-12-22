# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
自定义模块创建
·模块
   ·新建一个py文件,名称尽量不要与Python自带的标准樸块名称相同
·导入模块
 import 模块名称 [as别名]
 from 模块名称 import 函数/变量/类
'''
import math
print(id(math))
print(type(math))
print(math)
print(math.pi)
print('------------------------------')
print(dir(math))
print(math.pow(2,3),type(math.pow(2,3)))    #<class 'float'>  2的3次方
print(math.ceil(9.001))                     #ceil为天花板，向上取整
print(math.floor(9.9999))                   #floor为地板，向下取整

