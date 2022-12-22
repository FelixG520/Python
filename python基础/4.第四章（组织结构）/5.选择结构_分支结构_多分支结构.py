# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


     #多分支结构
'''中文语义：
       成绩是在90分以上吗？不是
       成绩是在80到90之间吗？不是
       成绩是在70到80之间吗？不是
       成绩是在60到70之间吗？不是
       成绩是在60分之下吗？是
    语法结构：
    if条件表达式1：
       条件执行体1
    elif条件表达式2：
       条件执行体2
    elif条件表达式N：
       条件执行体N
    【else：】
       条件执行体N+1.什么叫模块_模块化编程的好处
'''

#练习题
'''多分支结构，多选一进行
   从键盘录入一个整数成绩
   90-100  A
   80-89   B
   70-79   C
   60-69   D
   0-59    E
   小于0或大于100为非法整数（不是成绩的有效范围）
   '''


score=int(input('请输入一个成绩：'))
#判断
if score>=90 and score<=100:
    print('A级')
elif score>=80 and score<=89:       #elif是else if的缩写
    print('B级')
elif score>=70 and score<=79:
    print('C级')
elif score>=60 and score<=69:
    print('D级')
elif score>=0 and score<=59:
    print('E级')
else:
    print('对不起，成绩有误，不是成绩的有效范围')

#另一种独特的写法
score=int(input('请输入一个成绩：'))
#判断
if 90<=score<=100:
    print('A级')
elif 80<=score<=89:
    print('B级')
elif 70<=score<=79:
    print('C级')
elif 60<=score<=69:
    print('D级')
elif 0<=score<=59:
    print('E级')
else:
    print('对不起，成绩有误，不是成绩的有效范围')