# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
特殊方法
__len__() 通过重写__len__()方法,让内置函数len()的参数可以是自定义类型
__add__() 通过重写__add__()方法,可使用自定文对象具有“+”功能
__new__() 用于创建对象
__init__()对创建的对象进行初始化
'''

a=20
b=100
c=a+b   #两个整数类型的对象的相加操作
d=a.__add__(b)
print(c)
print(d)


class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name   #如果不写这个TypeError: unsupported operand type(s) for +: 'Student' and 'Student'

stu1=Student('张三')
stu2=Student('李四')
s=stu1+stu2   #实现了两个对象的加法运算（因为在Student类中编写__add__()特殊的方法）
print(s)
s=stu1.__add__(stu2)
print(s)


print('----------------------------------------------')
lst=[11,22,33,44]
print(len(lst))   #len是内容函数的长度
print(lst.__len__())