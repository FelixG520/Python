# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
面向对象的三大特征
封装:提高程序的安全性
    ·将数据(属性)和行为(方法)包装到类对象中。在方法内部对属性进行操作,在
     类对象的外部调用方法。这样，无需关心方法内部的具体实现细节,从而隔离了复杂度
    ·在Python中没有专门的修饰符用于属性的私有,如果该属性不希望在类对象外部被
     访问,前边使用两个＂_＂。
·继承:提高代码的复用性
·多态:提高程序的可扩展性和可维护性
'''


#点前面的箭头就可以对类进行封装
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动。')

#仍然可以使用被封装的类的方法和属性


car=Car('宝马x5')
car.start()
print(car.brand)


class Student:
    def __init__(self,age):
        self.set_age(age)
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if 0<=age<=120:
            self.__age=age
        else:
            self.__age=18


stu1=Student(150)
stu2=Student(30)
print(stu1.get_age())
print(stu2.get_age())

class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age    #年龄不希望在类的外部被使用，所以加了两个_
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
stu.show()
#在类的外部使用name和age
print(stu.name)
#print(stu.__age)   AttributeError: 'Student' object has no attribute '__age'
print(dir(stu))  #输出stu所有的属性和方法
'''
['_Student__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
'__weakref__', 'name', 'show']
'''
print(stu._Student__age)    #在类的外部可以通过  _Student__age进行访问




'''
君子协议
掩耳盗铃，全靠自觉
当遇见__时，说明不让访问，如果访问也行，就是不道德（狗头）'''
