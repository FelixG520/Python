# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！



print('----------------元组的遍历----------------')
t=('python','hello',90)
print('第一种获取元组元素的方式，使用索引')
print(t[0])
print(t[1])
print(t[2])
#print(t[3])       IndexError: tuple index out of range   超出元组范围

#元组支持切片操作
t2=t[0:3:2]
print(t2)

print('-------------遍历元组---------------')
for item in t:
    print(item)

for i in range(len(t)):
    print(i,t[i])

#使用enumerate()
for index,item in enumerate(t):
    print(index,'--->',item)

for index,item in enumerate(t,10):
    print(index,'--->',item)