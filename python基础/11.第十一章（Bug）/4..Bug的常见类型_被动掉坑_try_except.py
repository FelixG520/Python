# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
被动掉坑：程序代码逻辑没有错，只是因为用户错误操作或者一些“例外情况”而导致的程序崩溃
'''

print('------------------未经过优化，不可输入0和字符-----------------------')
a=int(input('请输入第一个整数：'))
b=int(input('请输入第二个整数：'))
result=a/b
print('结果为：',result)

#输入“q”        ValueError: invalid literal for int() with base 10: 'q'
#第二个数输入0    ZeroDivisionError: division by zero（分母不能为0）

'''python掉坑问题的解决方案
python提供了异常处理机制，可以在异常出现时即时捕获，然后内部“消化”，让程序继续运行'''


print('------------------经过优化，可输入0，不可输入字符-----------------------')
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
    print('结果为：', result)
except ZeroDivisionError:
    print('除数不能为0！！！')
print('程序结束')


print('------------------经过优化，可输入任意字符-----------------------')
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
    print('结果为：', result)
except ZeroDivisionError:
    print('除数不能为0！！！')
except ValueError:
    print('不能将字母串转换为数字')
except BaseException as e:
    print(e)

print('程序结束')