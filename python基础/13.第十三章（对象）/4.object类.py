# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
·object类
  ·object类是所有类的父类,因此所有类都有objcct类的属性和方法。
  ·内置函数dir()可以查看指定对象所有属性
  ·Object有一个_str_()方法，用于返回一个“对象的描述”，对应于内置函数str()经常用于print()方法，帮我们查看对象的信息
   所以我们经常会对_str_()进行重写
'''

class Student:
    pass
stu=Student()
print(dir(stu))   #内置函数dir()可以查看指定对象所有属性和方法
print(stu)        #<__main__.Student object at 0x000002538AD58550>


class Student1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):  #方法重写
        return '我的名字是{0}，今年{1}岁'.format(self.name,self.age)

stu=Student1('张三',20)
print(dir(stu))
print(stu)    #默认调用__str__()这样的方法
print(type(stu))