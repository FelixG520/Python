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