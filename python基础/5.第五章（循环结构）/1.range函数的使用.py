# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''内置函数range
   ·range()函数
       ·用于生成一个整数序列
       ·创建range对象的三种方式
           ·range（stop）————>创建一个【0，stop）之间的整数序列，步长为1
           ·range（start，stop）————>创建一个【start，stop）之间的整数序列，步长为1
           ·range（start，stop，step）————>创建一个【start，stop）之间的整数序列，步长为step
       ·返回值是一个迭代器对象
       ·range类型的优点：
           不管range对象表示的整数序列有多长所有range对象占用的内存空间都是相同的，因为仅仅需要存储start、stop、step，只有当用到range对象时，
           才会去计算序列中的相关元素
       ·in与not in判断整数序列中是否存在（不存在）指定的整数
        '''




#创建range对象的三种方式
#1.只有一个参数（小括号中只给了一个数）
r=range(10)      #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],默认从零开始，默认相差为1（步长为1）
print(r)         #range[0，stop）
print(list(r))   #用于查看range对象中的整数序列————>list是列表的意思

#2.给了两个参数（小括号中给了两个数）
r=range(1,10)    #指定了起始值，从1开始，到10结束（不包括10，左闭右开），默认步长为1
print(list(r))   #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#3.给了三个参数（小括号中给了三个数）
r=range(1,10,2)  #指定了起始值,指定了结束值，指定了步长
print(list(r))   #[1, 3, 5, 7, 9]

#判断指定的整数在序列中是否存在：in、not in
print(10 in r)       #False,10不在当前的r这个整数序列中
print(9 in r)        #Ture,9在当前的r这个整数序列中
print(10 not in r)   #Ture ,10不在当前的r这个整数序列中
print(9 not in r)    #False,9在当前的r这个整数序列中

print(range(1,20,1))
print(range(1,101,1))

print(list(range(1,20,1)))
print(list(range(1,101,1)))

