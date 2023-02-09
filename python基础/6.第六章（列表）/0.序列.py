'''
序列的相关操作
·序列的相加
-使用“+”实现两个同类型序列的相加操作，不会去除重复元素
- 注意事项:
·序列的类型要求是相同的，但是序列中元素的类型可以是不同的

·序列的相乘
-使用数字n乘以一个序列，将生成一个新的序列，新序列中的容会被重复n次
'''

s='Hello'
s2='World'
print(s+s2)

#注意事项 + 左右的数据类型相同，序列中元素的数据类型可以不同
lst=[10,20,30,'PHP']  #列表属于序列
#print(s+lst)    #TypeError: can only concatenate str (not "list") to str

print(s*5)
print('-----------------------------------------')
print('-'*40)

'''
序列的相关操作符与函数
操作符
X in s  :如果x是s的元素，结果为True，否则结果为False
X not in s  :如果x不是s的元素，结果为True，否则结果为False
len(s):序列s中元素的个数(即序列的长度)
max(s):序列s元素的最大值
min(s):序列s中元素的最小值
s.index(x):序列s中第一次出现元素x的位置
s.count(x):序列s中出现x的总次数

'''

s='helloworld'
print('e' in s)
print('e' not in s)
print(len(s))
print(max(s))
print(min(s))

print(s.index('o'))
print(s.count('o'))