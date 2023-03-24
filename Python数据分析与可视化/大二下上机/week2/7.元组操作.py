#7、请对元组元素'Google', 'Runoob', 1997, 2000使用Python对其进行定义等进行索引、遍历、删除等操作。
#遍历
t=('Google', 'Runoob', 1997, 2000)
for item in t:
    print(item,end=' ')
print()

#索引
#使用enumerate()
for index,item in enumerate(t):
    print(index,'--->',item)

#使用索引获取元素
print(t[0])
print(t[1])
print(t[2])
for index,item in enumerate(t,10):
    print(index,'--->',item)

#元组为不可变序列，因此删除要通过切片
t2=t[0:3:2]
print(t2)
