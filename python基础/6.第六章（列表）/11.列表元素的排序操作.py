# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

'''·列表元素的排序操作
    ·常见的两种方式
         ·调用sort（）方法，列表中有的所有元素默认按照从小到大的顺序进行排序，可以指定reverse=Ture进行降序排序
         ·调用内置函数sorted（），可以指定reverse=Ture，原列表不发生改变'''


#调用内置函数sort（），可以指定reverse=Ture，对原列表进行排序，原列表不发生改变
lst=[20,40,10,98,54]
print('排序前的列表',lst,id(lst))
#开始排序，调用列表对象的sort方法，升序排序
print('-------------调用列表对象的sort方法，升序排序-------------------')
lst.sort()
print('排序后的列表',lst,id(lst))

#通过指定关键字参数，将列表中的元素进行降序排序
print('-------------通过指定关键字参数，将列表中的元素进行降序排序--------------------')
lst.sort(reverse=True)    #reverse=Ture进行降序排序,reverse=False进行升序排序
print(lst)
lst.sort(reverse=False)
print(lst)


#调用内置函数sorted（），可以指定reverse=Ture，将产生一个新的列表对象
print('-----------------调用内置函数sorted（）,将产生一个新的列表对象-------------------')
lst=[20,40,10,98,54]
print('原序列',lst)
#开始排序
new_list=sorted(lst)
print(lst)
print(new_list)
#指定关键字参数，实现列表元素的降序排序
desc_list=sorted(lst,reverse=True)
print(desc_list)

