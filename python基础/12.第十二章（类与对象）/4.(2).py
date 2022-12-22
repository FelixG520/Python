# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
class Student:
    native_place='山东'             #直接写在类里的变量称为类属性
    #初始化方法
    def __init__(self,name,age):   #name和age都是变量
        self.name=name     #self.name称为实例属性，进行了赋值操作
        self.age=age

    #实例方法
    #在类之外定义的称为函数，在类之内定义的称为方法
    def eat(self):      #实例方法写self
        print('学生在吃饭...')
    #类方法
    @classmethod
    def cm(cls):         #类方法写cls
        print('使用了classmethod修饰，就是类方法')

    #静态方法
    @staticmethod
    def method():        #静态方法什么也不写
        print('使用了staticmethod修饰，就是静态方法')


#创建Student类的对象
stu1=Student('张三',20)
stu1.eat()            #对象名.方法名
print(stu1.name)
print(stu1.age)


print('------------------------------')
Student.eat(stu1)     #类名.方法名(类的对象) Student.eat(stu1)和stu1.eat()都是调用Student中的eat方法