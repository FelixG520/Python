# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
创建类的语法
class 类名：
      pass

就是C语言中的结构体
'''

class Student:    #Student为类的名称（类名）由一个或多个单词组成，每个单词的首字母大写，其余小写
    pass

#Python中一切皆对象Student是对象吗？内存有开空间吗？
print(id(Student))      #2613274967440
print(type(Student))    #<class 'type'>
print(Student)          #<class '__main__.Student'>



'''
·类的组成
  ·类属性
  ·实例方法
  ·静态方法
  ·类方法
  '''

class Student:
    native_place='山东'
    def eat(self):
        print('学生在吃饭。。。')  #定义在类内叫方法

def drink():    #定义在类外叫函数
    print('喝水')

class Student:
    native_place='山东'             #直接写在类里的变量称为类属性
    #初始化方法
    def __init__(self,name,age):   #name和age都是变量
        self.name=name     #self.name称为实例属性，进行了赋值操作
        self.age=age

    #实例方法
    #在类之外定义的称为函数，在类之内定义的称为方法
    def info(self):      #实例方法写self
        print('我的名字叫：',self.name,'年龄是：',self.age)
    #类方法
    @classmethod
    def cm(cls):         #类方法写cls
        print('使用了classmethod修饰，就是类方法')

    #静态方法
    @staticmethod
    def method():        #静态方法什么也不写
        print('使用了staticmethod修饰，就是静态方法')


