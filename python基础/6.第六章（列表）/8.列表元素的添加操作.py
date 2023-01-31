# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


#像列表的末尾添加一个元素
lst=[10,20,30]
print('添加元素之前',lst,id(lst))   #1876769500672
lst.append(100)   #append是追加的意思
print('添加元素之后',lst,id(lst))   #1876769500672  id相同，说明为同一个列表，并没有创建新列表


#在列表的末尾至少添加一个元素
lst2=['hello','world']
#将lst2作为一个元素添加到列表的末尾
print('将lst2作为一个元素添加到列表的末尾 ------ append')
lst.append(lst2)
print(lst)


##lst.append(lst2)   向列表的末尾一次性添加多个元素
print('向列表的末尾一次性添加多个元素 ------- extend')
lst.extend(lst2)
print(lst)


#在任意位置上添加一个元素
print('索引为1的位置添加90')
lst.insert(1,90)      #索引为1的位置添加90
print(lst)


#在任意位置上添加n多个元素(切片)
print('在任意位置上添加n多个元素')
lst3=['ture','false','world']
lst[1:]=lst3     #lst从索引为1开始一直到列表的最后(默认步长为1)
print(lst)       #lst被切的部分用lst3替换