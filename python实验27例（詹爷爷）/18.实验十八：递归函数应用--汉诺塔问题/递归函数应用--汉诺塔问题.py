# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
1.什么叫模块_模块化编程的好处.编写程序文件，输入参考代码
[root@master ~]# vi /opt/software/data/project/p_18/p_18.py
2.按i键进入编辑模式，输入以下代码
按Esc键退出编辑模式，输入“:wq”保存退出
3.执行程序文件
[root@master ~]# python3 /opt/software/data/project/p_18/p_18.py
'''


#encoding=utf-8
#递归函数应用--汉诺塔问题
def hannoi(num, src, dst, temp=None):      #递归算法
    if num < 1:
        return
    global times     # 声明用来记录移动次数的变量为全局变量
    #递归调用函数自身，先把除最后一个盘子之外的所有盘子移动到临时柱子上
    hannoi(num - 1, src, temp, dst)
    # 移动最后一个盘子
    print('The {0} Times move:{1}==>{2}'.format(times, src, dst))
    towers[dst].append(towers[src].pop())
    for tower in 'ABC':       # 输出 3 根柱子上的盘子
        print(tower, ':', towers[tower])
    times += 1
    # 把除最后一个盘子之外的其他盘子从临时柱子上移动到目标柱子上
    hannoi(num - 1, temp, dst, src)
times = 1        #用来记录移动次数的变量
n = 3                          #盘子数量
towers = { 'A':list(range(n, 0, -1)),'B':[ ],'C':[ ]  }       #初始状态，所有盘子都在 A 柱上
#A 表示最初放置盘子的柱子，C 是目标柱子，B 是临时柱子
hannoi(n, 'A', 'C', 'B')