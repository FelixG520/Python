# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

'''粗心导致的语法错误SyntaxError'''



print('-------------第一种--------------')
age=input('请输入您的年龄:')
print(type(age))
#if age>=18:          TypeError: '>=' not supported between instances of 'str' and 'int'
if int(age)>=18:
    print('成年人...')
else:
    print('未成年...')
print(type(int(age)))


print('-------------第二种--------------')
'''while i<10:    NameError: name 'i' is not defined
    print(i)'''

i=0
while i<10:  # NameError: name 'i' is not defined
    i+=1     #不加条件表达式会陷入死循环
    print(i)


print('-------------第三种--------------')
for i in range(3):
    uname=input('请输入用户名:')
    pwd=input('请输入密码:')
    #if uname='admin' and pwd='admin'    #=是赋值运算符，==是比较运算符
    if uname=='admin' and pwd=='admin':
        print('登陆成功！')
        break
    #else
    else:
        print('输入有误')
#else
else:
        print('对不起，三次均输入错误')


'''
·Bug 的常见类型
   ·粗心导致错误的自查宝典
     ·1.什么叫模块_模块化编程的好处.漏了末尾的冒号,如 if 语句,循环语句, else 子句等
     ·2.缩进错误,该缩进的没缩进,不该缩进的瞎缩进
     ·3.把英文符号写成中文符号,比如说:引号,冒号,括号
     ·4.字符串拼接的时候,把字符串和数字拼在一起
     ·5.没有定义变量,比如说 while 的循环条件的变量
     ·6.“==”比较运算符和”=”赋值运算符的混用
     '''