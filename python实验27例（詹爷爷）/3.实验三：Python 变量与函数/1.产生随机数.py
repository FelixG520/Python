# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

'''进入python shell
[root@master ~]# python3'''
#导入标准库
from random import randint
#本程序无输入处理
#产生一个 0~1000 的随机数，将其保存在变量 temp 中
temp = randint(0, 1000)   #randint 产生均匀分布的随机整数矩阵
#输出
print("产生的随机数为:",temp)