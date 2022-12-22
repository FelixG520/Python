# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

print('------------索引越界问题IndexError--------------')
lst=[11,22,33,44]
#print(lst[4])    IndexError: list index out of range
print(lst[3])


print('--------------append()方法的使用不熟练----------------')
lst=[]
#lst=append('A','B','C')       NameError: name 'append' is not defined     append()是列表的方法，应该是lst.append()v
#lst.append('A','B','C')       TypeError: append() takes exactly one argument (3 given)
lst.append('A')                #append()方法每次只能添加一个元素
lst.append('B')
lst.append('C')
print(lst)