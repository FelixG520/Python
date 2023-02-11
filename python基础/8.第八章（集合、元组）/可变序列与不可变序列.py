'''
可变序列 -- 内存地址不发生改变：列表，字典
'''

lst=[10,20,30]
print(id(lst))
lst.append(300)
print(id(lst))

'''
不可变序列 -- 内存地址发生更改：字符串，元组
'''
s='hello'
print(id(s))
s=s+' world'
print(id(s))
print(s)

'''
列表、元组、字典和集合的区别
数据类型       序列类型    是否重复                是否有序    字义符号
列表list      可变序列    可重复                    有序       []
元组tuple     不可变序列   可重复                     有序       ()
字典dict      可变序列    key不可重复value可重复      无序  {key:value)
集合set       可变序列    不可重复                    无序      {}

'''