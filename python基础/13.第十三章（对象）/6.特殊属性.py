# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''

特殊属性
__dict__  获得类对象或实例对象所绑定的所有属性和方法的字典

'''
class a:
    pass
class b:
    pass
class c(a,b):   #c继承了a和b
    def __init__(self,name):
        self.name=name
#创建C类的对象
x=c('Jack')    #x是C类型的实例对象
print(x.__dict__)#{'name': 'Jack'}


#print(dir(object))
class A:
    pass
class B:
    pass
class C(A,B):   #C继承了A和B
    def __init__(self,name,age):
        self.name=name
        self.age=age
class D(A):
    pass
#创建C类的对象
x=C('Jack',20)      #x是C类型的实例对象
print(x.__dict__)   #实例对象的属性字典


print('1',C.__dict__)   #类对象的实例字典
print('-------------------------------')
print('2',x.__class__)  #<class '__main__.C'>输出了对象所属的类
print('3',C.__bases__)  #(<class '__main__.A'>, <class '__main__.B'>) C类的父类类型的元组
print('4',C.__base__)   #<class '__main__.A'>输出第一个父类
print('5',C.__mro__)    #类的层次结构C继承了A，继承了B，继承了object
print('6',A.__subclasses__())  #A的子类的列表