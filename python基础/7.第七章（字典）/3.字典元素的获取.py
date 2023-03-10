# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''·字典中元素的获取
     ·[]————>举例：score['张三']
     ·get{}方法————>举例：score.get('张三')

   ·[]取值与使用get()取值的区别
      ·[]如果字典中不存在指定的key，抛出keyError
      ·get（）方法取值，如果字典中不存在指定的key，并不会抛出keyError而是返回None，
      可以通过参数设置默认的value，以便指定的key不存在时返回'''


#第一种方式，使用[]
scores= {'张三':100,'李四':98,'王五':45}
print(scores['张三'])
#print(scores['陈六'])         KeyError: '陈六'

#第二种方式，使用get()方法
print(scores.get('张三'))
print(type(scores.get('张三')))

print(scores.get('陈六'))       #None
print(scores.get('麻七',99))    #99是在查找‘麻七’所对的value不存在时，提供的一个默认值
