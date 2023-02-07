# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


#双分支结构if、else，二选一执行
'''中文语义：
   ·如果……不满足……就……
   ·如果中奖就领奖，没中奖就不领
   ·如果是妖怪就打，不是就不打
   ·如果是周末不上班，不是就上班
   语法结构：
    if条件表达式：
       条件执行体1
    else：
       条件执行体2
       '''

#从键盘录入一个整数，编写程序让计算机判断是奇数还是偶数
num=int(input('请输入一个整数：'))
#条件判断奇偶性
if num%2==0:
    print(num,'是偶数')
else:
    print(num,'是奇数')

result='偶数'if num%2==0 else '奇数'
print(result)