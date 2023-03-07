# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
1.什么叫模块_模块化编程的好处.编写程序，输入参考代码
[root@master ~]# vi /opt/software/data/project/p_13/p_13.py
2.按i键进入编辑模式，输入以下代码
按Esc键退出编辑模式，输入“:wq”保存退出
3.执行程序文件
[root@master ~]# python3 /opt/software/data/project/p_13/p_13.py
'''

#encoding=utf-8
maxNumber = int(input('请输入一个大于 2 的自然数：'))
lst = list(range(2, maxNumber))
#最大整数的平方根
m = int(maxNumber**0.5)
for index, value in enumerate(lst):
# 如果当前数字已大于最大整数的平方根，结束判断
    if value > m:
        break
#对该位置之后的元素进行过滤
    lst[index + 1:] = filter(lambda x: x % value != 0, lst[index + 1:])
    print(lst)



