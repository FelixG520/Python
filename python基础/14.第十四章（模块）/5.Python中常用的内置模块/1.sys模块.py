# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

'''
Python中常用的内置模块
sys:与Python解释器及其环境操作相关的标准库
time:提供与时间相关的各种函数的标准库
os:提供了访问操作系统服务功能的标准库
calendar:提供与日期相关的各种函数的标准库
urllib:用于读取来自网上(服务器)的数据标准库
json:用于使用JSON序列化和反序列化对象
re:用于在字符串中执行正则表达式匹配和替换
math:提供标准算术运算函数的标准库
decimal:用于进行精确控制运算精度、有效数位和四舍五入操作的十进制运算
1ogging:提供了灵活的记录事件、错误、警告和调试信息等目志信息的功能
'''

import sys                 #获取对象所占内存大小
print(sys.getsizeof(24))   #                   28个字节
print(sys.getsizeof(45))   #                   28个字节
print(sys.getsizeof(True)) #                   28个字节
print(sys.getsizeof(False))#                   24个字节


