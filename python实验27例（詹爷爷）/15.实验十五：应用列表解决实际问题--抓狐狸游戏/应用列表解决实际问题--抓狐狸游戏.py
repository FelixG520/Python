# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
1.什么叫模块_模块化编程的好处.编写程序文件，输入参考代码
[root@master ~]# vi /opt/software/data/project/p_15/p_15.py
2.按i键进入编辑模式，输入以下代码
按Esc键退出编辑模式，输入“:wq”保存退出
3.执行程序文件
[root@master ~]# python3 /opt/software/data/project/p_15/p_15.py
'''

#encoding=utf-8
import random
def catchMe(n=5, maxStep=10):
    '''模拟抓小狐狸，一共 n 个洞口，允许抓 maxStep 次如果失败，小狐狸就会跳到隔壁洞口'''
    #n个洞口,有狐狸为1，没有狐狸为0
    positions = [0] * n
    #狐狸的随机初始位置
    oldPos = random.randrange(0, n)
    positions[oldPos] = 1
    #玩家开始抓狐狸
    m = 1
    while m<=maxStep:
        # 判断输入正确
        print("第{}次".format(m))
    #抓maxStep次
        while True:
                try:
                    x =input('今天打算打开哪个洞口？（0-{0}）：'.format(n - 1))
                # 如果输入的不是数字，就会跳转到 except 部分
                    x=int(x)
                # 如果输入的洞口有效，结束这个循环，否则就继续输入
                    assert 0 <= x < n, '要按套路来啊，再给你一次机会。'
                    break
                except:
                    # 如果输入的不是数字，就执行这里的代码
                    print('要按套路来啊，再给你一次机会。')
    #判断有没有找到
        if positions[x] == 1:
            print('成功，我抓到小狐狸啦。')
            break
        else:
            print('今天又没抓到。')
    #小狐狸换洞口，洞口有两个可能
        if oldPos == 0:
            newPos = oldPos + 1
        elif oldPos == n - 1:    #为最后一个洞口
            newPos = 0
        else:
            newPos = oldPos + random.choice((-1, 1))
            positions[oldPos], positions[newPos] = 0,1     # 将位置更新
            m=m+1  # 次数+1.什么叫模块_模块化编程的好处
    else:
        print('放弃吧，你这样乱试是没有希望的。')
#启动游戏，开始抓狐狸吧
catchMe()


