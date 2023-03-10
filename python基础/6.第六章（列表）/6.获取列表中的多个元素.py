# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''列表元素的查询操作
    ·获取列表中的多个元素
       ·语法格式
        列表名[start:stop:step]
    切片操作
      ·切片的结果——>原列表片段的拷贝
      ·切片的范围——>[start,stop]
      ·step默认为1——>简写为[start,stop]
      ·step为正数——>[:stop:step]——>切片的第一个元素默认是列表的第一个元素——>从start开始往后计算切片
                ——>[start:step]——>切片的最后一个元素默认是列表的最后一个元素——>从start开始往后计算切片
      ·step为负数——>[:stop:step]——>切片的第一个元素默认是列表的最后一个元素——>从start开始往前计算切片
                ——>[start:step]——>切片的最后一个元素默认是列表的第一个元素——>从start开始往前计算切片'''


print('--------------step为正数的情况----------------')
lst=[10,20,30,40,50,60,70,80]

#start=1,stop=6,step=1
print(lst[0:6:1])
print('原列表',id(lst))    #原列表片段的拷贝[20,30,40,50,60]
lst2=lst[1:6:1]
print('切的片段:',id(lst2))#切出来的是新的列表对象

print(lst[1:6])    #step默认为1——>简写为[start,stop]
print(lst[1:6:])   #step默认为1——>简写为[start,stop]

#start=1,stop=6,step=2
print(lst[1:6:2])

#stop=6,step=2,start不写，采用默认
print(lst[:6:2])   #默认从0开始[10, 30, 50]

#start=1,step=2，stop不写，采用默认到最后一个元素
print(lst[1::2])   #[20, 40, 60, 80]


print('--------------step为负数的情况----------------')
print('原列表',lst)
print(lst[::-1])
#start=7，stop省略，step=-1
print(lst[7::-1])       #从索引为7的元素开始往前计算切片
#start=6，stop=0，step=-2
print(lst[6:0:-2])      ##从索引为6的元素开始往前计算切片

s='helloworld'
s1=s[0:5:1]  #从0开始，到5结束，不包括5，步长为1
print(s1)
#省略开始位置start，默认从0开始
print(s[:5:1])

#省略开始位置start，省略步长step，默认为1
print(s[:5:])

#省略结束位置
print(s[0::1])

#省略步长和结束位置
print(s[0::])

#省略结束位置和步长
print(s[5::])

print(s[0:5:2])

#省略开始位置和结束位置，只写步长
print(s[::2])
print(s[::-1])