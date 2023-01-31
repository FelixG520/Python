# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''·获取指定元素的索引
     index()·如查列表中存在N个相同元素，只返回相同元素中的第一个元素的索引
            ·如果查询的元素在列表中不存在，则会抛出ValueError
            ·还可以在指定的start和stop之间进行查找
    ·获取元素中的单个元素
     获取单个元素：·正向索引从0到N-1.什么叫模块_模块化编程的好处  举例：lst[0]
                ·你想索引从-N到-1.什么叫模块_模块化编程的好处  举例：lst[-N]
                ·指定索引不存在，抛出ValueError'''


lst=['hello','world',98]
print(lst.index('hello'))     #注意index后面是.而不是,



lst2=['hello','world',98,'hello']   #如查列表中存在N个相同元素，只返回相同元素中的第一个元素的索引
print(lst2.index('hello'))
#print(lst2.index('python'))         #如果查询的元素在列表中不存在，则会抛出ValueError
#print(lst2.index('hello',1,3))      #还可以在指定的start和stop之间进行查找,ValueError: 'hello' is not in list
print(lst2.index('hello',1,4))       #还可以在指定的start和stop之间进行查找