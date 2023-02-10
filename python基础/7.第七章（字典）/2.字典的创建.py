# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！



'''·字典的创建
     ·最常用的方式：使用花括号{}
       score={‘张三’：100，‘李四’：98，‘王五’：45}
     ·使用内置函数dict()
       dict(name='iack',age=20)'''

#第一种创建方式，使用花括号{}
score= {'张三':100,'李四':98,'王五':45}
print(score)
print(type(score))

d={10:'cat',20:'dog',30:'pet',20:'zoo'}  #key相同，值进行覆盖
print(d)

#第二种创建方式，使用内置函数dict()
student=dict(name='jack',age=20)
print(student)

score2= dict({'张三':100,'李四':98,'王五':45})
print(score2)

#zip函数的使用
lst1=[10,20,30,40]
lst2=['cat','dog','car','zoo']
zipobj=zip(lst1,lst2)
print(zipobj)#<zip object at 0x00000131A3915F80> -- zip对象
print(list(zipobj))#转列表

zipobj=zip(lst1,lst2)
d=dict(zipobj)
print(d)


#使用参数创建字典
d=dict(cat=10,dog=20,)  #参数（cat，dog...）相当于变量，不需要加引号
print(d)

t=(10,20,30)  #创建一个元组
print({t:10}) #元组做键，整数做值

#lst=[10,20,30]
#print({lst,10}) #列表做键 -- 报错，因为列表是可变序列


#空子典
d={}
print(d)

#字典的删除
del d
print(d)

#字典属于序列类型
d=dict(cat=10,dog=20,)
print('max:',max(t))
print('min:',min(t))
print('len:',len(t))
