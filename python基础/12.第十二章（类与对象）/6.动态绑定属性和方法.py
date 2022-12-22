# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
·Python是动态语言，在创建对象之后，可以动态的绑定属性和方法
'''

#定义一个类
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')


#创建类对象
stu1=Student('张三',20)
stu2=Student('李四',20)
print(id(stu1))     #2461858694480    已开了单独的内存空间
print(id(stu2))     #2461858788256    已开了单独的内存空间


print('----------------为stu1动态绑定性别属性--------------------')   #动态绑定的属性只适用于当前绑定的这个对象
stu1.gender='女'
print(stu1.name,stu1.age,stu1.gender)
print(stu2.name,stu2.age)


##gender只属于stu1，stu2不允许使用；但name和age是stu1，stu2共有的
#print(stu2.name,stu2.age,stu2.gender)   AttributeError: 'Student' object has no attribute 'gender'


print('-------------没有绑定动态方法------------------')
stu1.eat()
stu2.eat()


print('-------------为stu1单独绑定show方法------------------')
def show():
    print('定义在类之外的，称为函数')
stu1.show=show
stu1.show()

#stu2没有绑定show方法(定义时为函数，调用时为方法)
#stu2.show()   AttributeError: 'Student' object has no attribute 'show'