# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！



s1={10,20,30,40}
s2={20,30,40,50,60}
#交集intersection()     &
print('------------交集&--------------')
print(s1.intersection(s2))
print(s1 & s2)          #intersection()与&等价
print(s1)
print(s2)               #原集合没有发生任何改变


#并集union()   |
print('------------并集|--------------')
print(s1.union(s2))
print(s1 | s2)          #union()与|等价
print(s1)
print(s2)               #原集合没有发生任何改变

#差集difference()    -
print('------------差集---------------')
print(s1.difference(s2))
print(s1 - s2)
print(s2.difference(s1))
print(s1)
print(s2)               #原集合没有发生任何改变

#对称差集^*(去掉交集之外两个集合的其他元素)
print('------------对称差集^---------------')
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s1)
print(s2)               #原集合没有发生任何改变
