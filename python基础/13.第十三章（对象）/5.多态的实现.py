# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
·多态
  ·简单的说，多态就是“具有多种形态”，它指的是：即便不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用方法，
   在运行过程中根据变量所引用的对象的类型，动态决定调用哪个对象中的方法。
'''

class Animal(object):
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼...')
#Dog和Cat继承了Animal

class Person: #默认继承object
    def eat(self):
        print('人吃五谷杂粮')

#定义一个函数
def fun(obj):
    obj.eat()
#开始调用函数
fun(Cat())   #这里的Cat()是匿名对象，也可以是Cat().eat()
fun(Dog())
fun(Animal())
print('-------------------------------')
fun(Person())



'''
·静态语言（java）与动态语言（python）
  ·静态语言和动态语言关于多态的区别
     ·静态语言实现多态的三个必要条件
       ·继承
       ·方法重写
       ·父类引用指向子类对象
  ·动态语言的多态崇尚“鸭子类型“当看到一只鸟走起来像鸭子、游泳起来像鸭子、收起来也像鸭子,那么这只鸟就可以被称为鸭子。
   在鸭子类型中,不需要关心对象是什么类型,到底是不是鸭子,只关心对象的行为。

'''