# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
类属性、类方法、静态方法
·类属性:类中方法外的变量称为类属性,被该类的所有对象所共享
·类方法:使用@classmethod 修饰的方法,使用类名直接访问的方法
·静态方法:使用@staticmethod 修饰的主法,使用类名直接访问的方法
 print(Student.native_place)    #访问类属性
 Student.cm()                   #调用类方法
 Student.sm()                   #调用静态方法
'''


class Student:
    native_place='山东'             #直接写在类里的变量称为类属性
    #初始化方法
    def __init__(self,name,age):   #name和age都是变量
        self.name=name             #self.name称为实例属性，进行了赋值操作
        self.age=age

    #实例方法（传的是self）
    #在类之外定义的称为函数，在类之内定义的称为方法
    def eat(self):      #实例方法写self
        print('学生在吃饭...')
    #类方法（传得是class）
    @classmethod
    def cm(cls):         #类方法写cls
        print('使用了classmethod修饰，就是类方法')

    #静态方法
    @staticmethod
    def method():        #静态方法什么也不写
        print('使用了staticmethod修饰，就是静态方法')


#类属性的使用方式
#print(Student.native_place)
stu1=Student('张三',20)     #stu1,stu2是Student类的实例对象
stu2=Student('李四',30)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place='陕西'
print(stu1.native_place)
print(stu2.native_place)


print('----------------类方法的使用------------------')
Student.cm()

print('----------------静态方法的使用------------------')
Student.method()