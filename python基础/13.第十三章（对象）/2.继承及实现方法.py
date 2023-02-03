# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
·继承
   ·语法格式
   class 子类类名（父类1，父类2...）：
        pass
   ·如果一个类没有继承任何类，则默认继承object
   ·Python支持多继承
   ·定义子类时，必须在其构造函数中调用父亲的构造函数
'''


#继承的代码实现
#定义Person类
class Person(object):                 #object可写可不写，Person继承了object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print('姓名:{0},年龄:{1}'.format(self.name,self.age))
#定义Person的子类
class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)   #super()是用来调用父类的一个方法
        self.stu_no=stu_no    #self是Student类的对象

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear

stu=Student('张三',20,'1001')
teacher=Teacher('李四',34,10)

stu.info()   #info是从Person类继承过来的
teacher.info()


#多继承
class A(object):
    pass

class B(object):
    pass

class C(A,B):   #C有两个父类
    pass