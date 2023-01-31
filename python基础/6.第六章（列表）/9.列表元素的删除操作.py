# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

'''列表元素的删除操作
    删除操作：
          ·remove（）
                  ·一次删除一个元素
                  ·重复元素只删除第一个
                  ·元素不存在抛出valueError
          ·pop（）
                  ·删除一个指定索引位置上的元素
                  ·指定索引不存在抛出IndexError
                  ·不指定索引，删除列表中最后一个元素
          ·切片
                  ·一次至少删除一个元素
          ·clear（）
                  ·清空列表
          ·del
                  ·删除列表'''


lst=[10,20,30,40,50,60,30]
print('删除一个具体的元素 ----- remove')
lst.remove(30)   #从列表中移除一个元素，如果有重复元素,只移第一个
print(lst)
#lst.remove(100)   ValueError: list.remove(x): x not in list



#pop()删除一个指定索引位置上的元素
print('删除一个指定索引位置上的元素 ----- pop')
lst.pop(1)
print(lst)
#lst.pop(5)      IndexError: pop index out of range
print('不指定索引，删除列表中最后一个元素')
lst.pop()
print(lst)

#至少删除一个元素,将产生一个新的列表对象
print('至少删除一个元素,将产生一个新的列表对象')
new_list=lst[1:3]
print('原列表',lst)
print('切片后的函数',new_list)

#至少删除一个元素，不产生一个新的列表对象
print('至少删除一个元素，不产生一个新的列表对象')
lst[1:3]=[]
print(lst)


#清楚列表中的所有元素
print('清楚列表中的所有元素')
lst.clear()
print(lst)

#del语句将清除列表
print('del语句将清除列表')
del lst
#print(lst)   name 'lst' is not defined