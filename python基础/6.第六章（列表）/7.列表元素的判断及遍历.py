# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。



print('p' in 'python')      #True
print('k' not in 'python')  #True
print()

lst=[10,20,'python','hello']
print(10 in lst)
print(100 in lst)
print(10 not in lst)
print(100 not in lst)
#遍历列表中的元素
print('------------遍历列表中的元素------------------')
for item in lst:                #item为可迭代对象，字符串和列表为可迭代对象
    print(item)

