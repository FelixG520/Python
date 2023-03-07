# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
1.什么叫模块_模块化编程的好处.编写程序文件，输入参考代码
[root@master ~]# vi /opt/software/data/project/p_17/p_17.py
2.按i键进入编辑模式，输入以下代码
按Esc键退出编辑模式，输入“:wq”保存退出
3.执行程序
[root@master ~]# python3 /opt/software/data/project/p_17/p_17.py
'''
#encoding=utf-8
def climbStairs1(n):
    # 递推法
    a=1
    b=2
    c=4
    for i in range(n - 3):
        c,b,a=a+b+c,c,b
    return c


def climbStairs2(n):
#递归法
    first3 = {1: 1, 2: 2, 3: 4}
    if n in first3.keys():
            return first3[n]
    else:
        return climbStairs2(n - 1) +\
                      climbStairs2(n-2) + \
                      climbStairs2(n-3)


print(climbStairs1(15))
print(climbStairs2(15))