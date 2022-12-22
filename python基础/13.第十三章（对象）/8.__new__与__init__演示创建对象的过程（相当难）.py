# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
class Person(object):

    def __new__(cls,*args,**kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))   #2458314060544
        obj=super().__new__(cls)
        print('创建的对象的id为:{0}',format(id(obj)))                 #2458321267440
        return obj


    def __init__(self,name,age):
        print('__init__被调用了，self的id值为:{0}'.format(id(self)))   #2458321267440
        self.name=name
        self.age=age

print('object这个类对象的id为:{0}'.format(id(object)))        #140714380127056
print('Person这个类对象的id为:{0}'.format(id(Person)))        #2458314060544


#创建Person类的实例对象
p1=Person('张三',20)
print('p1这个Person类的实例对象的id为:{0}'.format(id(p1)))     #2458321267440