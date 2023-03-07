# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

'''2、编写程序，输入一个学生的成绩，
如果是90分以上，打印出“A”的评语；
80分以上的，打印出“B”；70分以上的，打印出“C”；
60分以上的，打印出“D”；
不及格的打印出”E”
实现步骤：
1.什么叫模块_模块化编程的好处.编写程序文件
[root@master~]#vi/opt/software/data/project/p_5/p_5_2.py
2.按i键进入编辑模式，输入以下代码
修改完成后按Esc键退出编辑模式，输入“:wq”保存退出文档
3.执行程序文件
[root@master~]#python3/opt/software/data/project/p_5/p_5_2.py'''



print('这是一个可以打印与你的分数相关的分数的程序,你的分数范围是0-100')
x=int(input('请输入一个成绩：'))
while True:       #while循环，要用break，否则陷入循环；不用while循环不用写break，如果写了报错，因为不是while循环
    if x>100:
        print('对不起，成绩有误，不是成绩的有效范围')
    if 90<x<=100:
        print("A")
        break
    if 80<x<=90:
        print("B")
        break
    if 70<x<=80:
        print("C")
        break
    if 60<x<=70:
        print("D")
        break
    if 0<=x<60:
        print("E")
        break


print('----------------个人实操-----------------')
score=int(input('请输入一个成绩：'))
#判断
if score>=90 and score<=100:
    print('A')
elif score>=80 and score<=89:       #elif是else if的缩写
    print('B')
elif score>=70 and score<=79:
    print('C')
elif score>=60 and score<=69:
    print('D')
elif score>=0 and score<=59:
    print('E')
else:
    print('对不起，成绩有误，不是成绩的有效范围')

#另一种独特的写法
score=int(input('请输入一个成绩：'))
#判断
if 90<=score<=100:
    print('A')
elif 80<=score<=89:
    print('B')
elif 70<=score<=79:
    print('C')
elif 60<=score<=69:
    print('D')
elif 0<=score<=59:
    print('E')
else:
    print('对不起，成绩有误，不是成绩的有效范围')