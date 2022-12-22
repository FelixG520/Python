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


print('-------------遍历元组---------------')
for item in t:
    print(item)

