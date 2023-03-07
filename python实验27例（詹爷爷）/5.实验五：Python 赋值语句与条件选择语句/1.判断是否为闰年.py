# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''1.什么叫模块_模块化编程的好处、编写程序,实现输入一个年份，判断它是否是闰年，输出判断结果。
1.什么叫模块_模块化编程的好处.编写执行程序
[root@master~]#vi/opt/software/data/project/p_5/p_5_1.py

2.按i键进入编辑模式，输入以下代码
修改完成后按Esc键退出编辑模式，输入“:wq”保存退出文档
3.执行程序文件
[root@master~]#python3/opt/software/data/project/p_5/p_5_1.py
'''

y=int(input("Please enter the year:"))    #四年一闰；百年不闰，四百年再闰
if(y%4==0 and y%100!=0 & y%400==0):       #and也可用&替代
    print(y, "是闰年")
else:
    print(y, "不是闰年")

