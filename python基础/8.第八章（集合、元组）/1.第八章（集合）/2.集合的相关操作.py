# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！



'''·集合元素的判断操作
      ·in或not in


   ·集合元素的新增操作
      ·调用add()方法，一次添加一个元素
      ·调用update()方法，一次至少添加一个元素


   ·集合元素的删除操作
      ·调用remove()方法，一次删除一个指定元素，如果指定的元素不存在抛出KeyEror
      ·调用discard()方法，一次删除一个指定元素，如果指定的元素不存在不抛出KeyEror
      ·调用pop()方法，一次只删除一个任意元素，不能添加参数，只能是无参的，否则抛出TypeError: pop() takes no arguments (1.什么叫模块_模块化编程的好处 given)
      ·调用clear()方法，清空集合
      '''


print('-----------------集合元素的判断操作---------------------')
a={10,20,30,405,60}
print(10 in a)
print(100 in a)
print(10 not in a)
print(100 not in a)

print('------------------集合元素的新增操作--------------------')
a.add(80)      #add()一次添加一个元素
print(a)

#添加元素[]{}()都可以
a.update({200,400,300})     #update()一次至少添加一个元素
print(a)
a.update([100,99,8])
print(a)
a.update((78,64,56))
print(a)


print('------------------集合元素的删除操作--------------------')
a.remove(100)
print(a)
#a.remove(500)    KeyError: 500

a.discard(500)     #有就删，没有也不抛异常
print(a)

a.pop()            #一次只删除一个任意元素
print(a)
#a.pop(400)        TypeError: pop() takes no arguments (1.什么叫模块_模块化编程的好处 given)

a.clear()           #清空集合
print(a)

#del a
#print(a)

b={88,945,456,54,56,564,12,35,3351}
for index,item in enumerate(b):
    print(index,'--->',item)