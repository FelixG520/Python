# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

'''items=['Fruits','Books','Others']
   prices[96,78,85]


            {'Fruits':96,'Books':78,'Others':85}
·内置函数zip()
   ·用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表
  '''


items=['Fruits','Books','Others']
prices=[96,78,85]
d={item:price for item,price in zip (items,prices)}           #{'Fruits': 96, 'Books': 78, 'Others': 85}
print(d)

prices=[96,78,85]
d={item.upper():price for item,price in zip (items,prices)}   #{'FRUITS': 96, 'BOOKS': 78, 'OTHERS': 85}变大写
print(d)

#若两个列表中的元素数量不一样
print('---------------若两个列表中的元素数量不一样----------------')
items=['Fruits','Books','Others']
prices=[96,78,85,100,120]
d={item:price for item,price in zip (items,prices)}        #{'Fruits': 96, 'Books': 78, 'Others': 85}
print(d)