# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
·获取字典试图的三个方法
      获取字典视图：
          ·1.什么叫模块_模块化编程的好处.keys()————>获取字典中所有key
          ·2.values()————>获取字典中所有value
          ·3.items()————>获取字典中所有key，value对
'''



scores= {'张三':100,'李四':98,'王五':45}
#获取所有的key
print('------------------获取所有的key--------------------')
keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys))     #将所有的key组成的视图转成列表


#获取所有的value
print('------------------获取所有的value--------------------')
values=scores.values()
print(values)
print(type(values))
print(list(keys))


#获取所有的key-value值
print('------------------获取所有的key-value值--------------------')
items=scores.items()
print(items)
print(list(items))    #转换之后的列表元素是由元组组成

