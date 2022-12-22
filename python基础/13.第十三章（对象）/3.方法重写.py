# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
·方法重写
  ·如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其（方法体）进行重新编写
  ·子类重写后的方法中可以通过super().xxx()调用父类中被重写的方法
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
        self.stu_no=stu_no

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear

stu=Student('张三',20,'1001')
teacher=Teacher('李四',34,10)

stu.info()
teacher.info()
'''
教师没有输出教龄（teachofyear）
学生没有输出学号（stu_no）
因为info()完不成这个要求，因为父类之中既没有学号，也没有教龄，没有办法输出
子类想输出自己独有的东西，父类已经不能提供需求，子类需要重写，即方法重写'''


#方法重写
class Person(object):                 #object可写可不写，Person继承了object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)
#定义Person的子类
class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)   #super()是用来调用父类的一个方法
        self.stu_no=stu_no
    def info(self):
        super().info()            #先执行父类  张三 20
        print('学号',self.stu_no)  #再执行子类  1001

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear
    def info(self):
        super().info()
        print('教龄',self.teachofyear)

stu=Student('张三',20,'1001')
teacher=Teacher('李四',34,10)


print('-------------方法重写------------------')
stu.info()
print('-------------方法重写------------------')
teacher.info()

