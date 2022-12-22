# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
什么叫模块
·模块
   ·模块英文为Modules
   ·函数与模块的关系
      ·一个模块中可以包含N多个函数
   ·在Python中一个扩展名为py的文件就是一个模块
   ·使用模块的好处
      ·方便其它程序和脚本的导人非使用
      ·避免函数名和变量名冲突
      ·提高代码的可维护性
      ·提高代玛的可重用性
'''


#一个python文件就是一个模块，可以输入各种代码（函数、类、语句）
def fun():
    pass
def fun2():
    pass

class Student:
    native_place='山东'         #类属性
    def eat(self,name,age):    #实例方法
        self.name=name         #实例属性
        self.age=age
    @classmethod               #类方法
    def cm(cls):
        pass
    @staticmethod              #静态方法
    def sm():
        pass
