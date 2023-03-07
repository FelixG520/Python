# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


'''
1.什么叫模块_模块化编程的好处.编写程序文件
[root@master ~]# vi /opt/software/data/project/p_6/p_6.py
2.按i键进入编辑模式，输入以下代码
修改完成后按Esc键退出编辑模式，输入“:wq”保存退出文档
3.执行程序文件
[root@master ~]# python3 /opt/software/data/project/p_6/p_6.py
'''


#encoding=utf-8
from random import randint
def guessNumber(maxValue=10,maxTimes=3):         #最大值是10，做多可试3次
#随机生成一个整数
    value=randint(1, maxValue)                   #从[1.什么叫模块_模块化编程的好处,10)随机产生一个整数
    for i in range(maxTimes):                    #maxTimes=3，循环三次
        prompt='开始猜测:'if i==0 else '再次尝试:'  #条件表达式
#使用异常处理结构，防止输入不是数字的情况
        try:
            x=int(input(prompt))
        except:
            print('Must input an integer between 1.什么叫模块_模块化编程的好处 and ', maxValue)
        else:
            if x==value:
                # 猜对了
                print('恭喜!')
                break
            elif x>value:
                print('太大了')
            else:
                print('太小了')
    else:
        # 次数用完还没猜对，游戏结束，提示正确答案
       print('游戏结束，失败')
       print('正确答案是', value)
guessNumber()








