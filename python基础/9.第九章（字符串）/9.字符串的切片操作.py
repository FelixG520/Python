# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
·字符串是不可变类型
  ·不具备增、删、改等操作
  ·切片操作将产生新的对象
'''

s='hello,Python'
s1=s[:5]         #由于没写起始位置默认从索引为零开始
print(s1)

s2=s[6:]         #由于没写结束为止默认从索引为6开始一直到最后
print(s2)

s3='!'
newstr=s1+s3+s2
print(newstr)


print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(newstr))


print('---------------切片[start:end:step]-------------------')
print(s[1:5:1])      #从索引1开始结束到5（不包含5），步长为1
print(s[::2])        #从0开始一直到最后结束，步长为2
print(s[::-1])       #默认从最后开始，到字符串的第一个元素结束，步长为1，即将元素倒置
print(s[-6::1])      #从索引-6开始到字符串的最后一个元素结束，步长为1

