# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
·对象的创建又称为类的实例化
·语法:
   实例名=类名()
·例子：
   stu=Student()
·意义：有了实例，就可以调用类中的内容
'''

class Student:                     #Student为类的名称（类名）由一个或多个单词组成，每个单词的首字母大写，其余小写
    native_place='山东'             #直接写在类里的变量称为类属性
    #初始化方法
    def __init__(self,name,age):   #name和age都是变量
        self.name=name     #self.name称为实例属性，进行了赋值操作，将局部变量的name的值赋给实体属性
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


#创建Student类的对象
stu1=Student('张三',20) #根据类对象创建出来的就是实例对象   stu1就是实例对象，根据类对象(Student就是类对象)创建出来
print(id(stu1))        #3029073261472   换成16进制就是2C142D5F3A0
print(type(stu1))      #<class '__main__.Student'>
print(stu1)            #<__main__.Student object at 0x000002C142D5F3A0>
print('-------------------------------------')
print(id(Student))     #Student就是类对象
print(type(Student))
print(Student)