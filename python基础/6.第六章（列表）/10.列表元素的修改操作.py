# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


'''列表元素的修改操作
  ·列表元素的修改操作
     ·为指定索引的元素赋予了一个新值
     ·为指定的切片赋予一个新值
     '''


lst=[10,20,30,40]
#一次修改一个值
print('-------------一次修改一个值------------------')
lst[2]=100
print(lst)



#为指定的切片赋予一个新值
print('-------------为指定的切片赋予一个新值------------------')
lst[1:3]=[300,400,500,600]
print(lst)