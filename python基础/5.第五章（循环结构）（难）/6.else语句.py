# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！


#if条件表达式不成立时执行else
#while或for循环没有碰到break时执行else


print('用for')
for item in range(3):
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print('对不起，三次密码均输入错误')



print('用while')
a=0
while a<3:
   #条件执行体（循环体）
    pwd=input('请输入密码：')
    if pwd =='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
       # 改变变量
        a+=1
else:
    print('对不起，三次密码均输入错误')