# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''·集合
      ·python语言提供的内置数据结构
      ·与列表、字典一样都属于可变类型的序列
      ·集合是没有value的字典

    ·集合的创建
      ·直接{}
          s={'Python','hello',90}
      ·使用内置函数set()
          s=set(range(6))
          print(s)
          print(set([3,4,53,56]))
          print(set((3,4,43,435)))
          print(set('Python'))
          print(set({124,3,4,4,5}))
          print(set())
集合
-Python中的集合与数学中集合的概念一致
- 集合可分为可变集合set与不可变集合frozenset-集合与字典中的key一致都是无序的
- 集合中的元素要求唯一
- 集合中只能存储不可变数据类型(字符串、整数、浮点数、元组)-集合使用分定义，元素之间使用逗号进行分隔

完全等价数学中的集合
和列表本质上是无序性，列表是有序的
'''


print('-----------第一种创建方式，使用{}--------------')
s={2,3,4,5,5,6,7,7}    #元素的唯一性，所以输出一个5，一个7
print(s)


print('-----------第二种创建方式，使用内置函数set()--------------')
s1=set(range(6))
print(s1,type(s1))

#可以把()[]{}都转化为set类型
s2=set([3,4,53,56])     #集合中的元素是无序的
print(s2,type(s2))

s3=set((3,4,43,435))
print(s3,type(s3))

s4=set('Python')
print(s4)

s5=set({124,3,4,4,5})
print(s5,type(s5))

print('--------------定义一个空集合---------------')
s6={}
print(type(s6))        #<class 'dict'>字典类型，不能直接用{}
s7=set()
print(s7,type(s7))     #<class 'set'>

#序列操作
print('max:',max(s))
print('min:',min(s))
print('len:',len(s))
print('9在集合中是否存在？',(9 in s))
print('9在集合中是否不存在？',(9 not in s))

