# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍

'''    ·获取元素中的单个元素
     获取单个元素：·正向索引从0到N-1.什么叫模块_模块化编程的好处  举例：lst[0]
                ·逆向索引从-N到-1.什么叫模块_模块化编程的好处  举例：lst[-N]
                ·指定索引不存在，抛出ValueError
(N是元素的个数)'''



lst=['hello','world',98,'hello','world',234]
#获取索引为2的元素
print(lst[2])    #正向索引
print(lst[-3])   #逆向索引
#获取索引为10的元素
#print(lst[10])   #IndexError: list index out of range（超出范围）
