# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

'''finally块无论是否发生异常都会被执行，能常用来释放try块中申请的资源'''

try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
except BaseException as e:#BaseException起个别名e
    print('出错了',e)
else:
    result=a/b
    print('计算结果为',result)
finally:
    print('谢谢您的使用')