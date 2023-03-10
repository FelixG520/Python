# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！



'''列表生成式：生成列表的公式
     ·语法格式：
       [i*i for i in range(1,10)]
         ·i*i    表示列表元素的表达式
         ·i      自定义变量
         ·range（）可迭代对象
     ·注意事项：表示列表元素的表达式中，通常包含自定义变量'''
import random

for i in range(10):
    print(i,end=' ')
print()

#放进列表里
lst=[i for i in range(10)]
print(lst)
lst=[i*i for i in range(10)]
print(lst)

lst=[random.randint(1,100) for _ in range(10)]#用不到循环变量（item），就用_
print(lst)
#列表中的元素的值为2，4，6，8，10
print('-------------列表中的元素的值为2，4，6，8，10-------------------')
lst2=[i*2 for i in range(1,11)]
print(lst2)

#从列表中选择符合条件的元素组成新的列表
lst=[i for i in range(10) if i%2==0] #0-10的偶数
print(lst)