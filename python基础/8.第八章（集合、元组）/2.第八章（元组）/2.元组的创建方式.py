# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''·元组的创建方式
     ·直接小括号
        t=(’python‘,'hello',90)    小括号可省略
     ·使用内置函数tuple()
        t=tuple((’python‘,'hello',90))
     ·只包含一个元组的元素需要使用逗号和小括号
        t=(10,)
        '''


print('----------------第一种，使用小括号-------------------')
t=('python','hello',90)
print(t)
print(type(t))

t2='python','hello',90    #省略了小括号
print(t2)
print(type(t2))
print('----------------第二种，使用内置函数tuple()-------------------')
t=tuple(('python','hello',90))
print(t)
print(type(t))


print('------------·只包含一个元组的元素需要使用逗号和小括号----------------')
t3=('python')
print(t3,type(t3))    #不加逗号<class 'str'>
t3=('python',)
print(t3,type(t3))    #加逗号<class 'tuple'>


print('-------------空元组的创建---------------')
#空列表
lst=[]
lst1=list()
#空子典
d={}
d1=dict()
#空元组
t4=()
t5=tuple()
print('空列表',lst,lst1)
print('空子典',d,d1)
print('空元组',t4,t5)