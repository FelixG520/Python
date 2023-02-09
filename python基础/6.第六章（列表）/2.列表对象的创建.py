# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
                                                 #列表的创建
'''列表需要使用中括号[],元素之间用英文的逗号进行分离
      ·列表的创建方式
        ·使用中括号
        ·使用内置函数list（）'''

#创建列表的第一种方式，使用[]
lst1=['hello','world',98]
#创建列表的第二种方式，使用内置函数list（）
lst2=list(['hello','world',98])
print(lst2)

lst3=list(range(1,10,2))
print(lst3)

print(lst3+lst1+lst2)
print(lst3*3)

print(len(lst3))
print(max(lst3))
print(min(lst3))

lst4=list('helloworld')
print(lst4.count('o'))
print(lst4.index('o'))