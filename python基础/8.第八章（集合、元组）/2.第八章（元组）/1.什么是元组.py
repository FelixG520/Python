# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''·元组
     ·python内置的数据结构之一，是一个不可变序列


   ·不可变序列与不可变序列
     ·不变可变序：字符串、元组
       ·不变可变序列：没有增、删、改
     ·可变序列：列表、字典
       ·可变序列：可以对序列执行增、删、改操作，对象地址不发生更改

和列表外观上只是括号的不同

       '''


t=('hello',[10,20,30],'python','world')
print(t)

t=tuple('helloworld')
print(t)

t=tuple([10,20,30,40])
print(t)

t=tuple(range(1,10))
print(t)

#元组的相关操作
print('10在元组中是否存在：',(10 in t))
print('10在元组中不存在：',(10 not in t))
print('max:',max(t))
print('min:',min(t))
print('len:',len(t))
print('t.index:',t.index(1))
print('t.count:',t.count(3))

x=(10)
print(x,type(x))

y=(10,) #元组只有一个元素，逗号不能省
print(y,type(y))

#元组的删除
del t
print(t)