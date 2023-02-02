# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

'''
·字符串的比较操作
  ·运算符:>,>=,<,<=,==,!=
  ·比较规则:首先比较两个字符串中的第一个字符,如果相等则继续比较下一个字符,依次比较下去,直到两个字符串中的字符不相等时,其比较结果就是两个字符串的比较结果,
          两个字符串中的所有后续字符将不再被比较
  ·比较原理:两上字符进行比较时,比较的是其ordinal value(原始值)，调用内置函数ord可以得到指定字符的ordinal value。内置函数ord对应的是内置函数chr,
          调用内置函数chr时指定ordinal value可以得到其对应的字符
'''

print('apple'>'app')    #True
print('apple'>'banana') #False   相当于97>98

#比较的是其ordinal value(原始值) -- 类似ASCII码值
print(ord('a'),ord('b'))
print(chr(97),chr(98))
print(ord('高'))
print(chr(39640))


''' == 与 is 的区别
    ==比较的是value
    is比较的是id
  '''
a=b='Python'
c='Python'
print(a==b)
print(b==c)
print(a is b)
print(a is c)
print(id(a),id(b),id(c))     #采用了驻留机制