# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
           #数据类型
#·整数类型-->int-->98
#·浮点数类型-->float-->3.14159
#·布尔类型-->bool-->True、False
#·字符串类型-->str-->’愿得少华刹那，开得满树芳华繁花‘


                                   #整数类型int
#英文为integer，简写为int，可以表示正数、负数和零
n1=90
n2=-76
n3=0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
#整数的不同进制表示方式
print('十进制',118)             #十进制-->默认的进制
print('二进制',0b10101111)      #二进制-->以0b开头
print('八进制',0o176)           #八进制-->以0o开头
print('十六进制',0x1EAF)         #十六进制-->以0x开头

num=987
num2=0b10101
num3=0o765
num4=0x87ABF
print(num)
print(num2)
print(num3)
print(num4)


                                    #浮点类型float
'''
- 浮点数类型
    ·表示带有小数点的数值
    ·浮点数由整数部分和小数部分组成
    ·Python中浮点数类型必须带有小数部分，小数部分可以是0
    ·浮点数可以使用科学记数法表示
    ·两个浮点数运算，有一定概率运算结果后增加一些“不确定的”尾数
    ·使用内置函数round()限定运算结果需要保留的小数位数
    ·不可变数据类型
'''
#浮点数整数部分和小数部分组成
a=3.14159
print(a,type(a))#float类型
#浮点数存储不确定性
#使用浮点数进行计算时，可能会出现小数位数不确定的情况
n1=1.1
n2=2.2
print(n1+n2)#输出3.3000000000000003计算机采用二进制进行存储，因此存储浮点数不精确，存在误差
print(round(n1+n2,1)) #保留一位小数
#解决方案
#导入模块decimal
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))
#不是所有的浮点数都会出现这种情况
n3=2.1
print(n1+n3)

                                        #布尔类型bool
#用来表示真或假的值
f1=True
f2=False
print(f1,type(f1))
print(f2,type(f2))
#True表示真，False表示假
#布尔值可以转化为整数
print(f1+1)#Ture表示1
print(f2+1)#False表示0




'''
- 复数类型
    ·Python中的复数与数学中的复数形式完全一致
    ·复数与实部和虚部组成
    ·j是复数的一个基本单位,被定义为j = √-1,又称“虚数单位”
    ·.real获取实数部分,imag获取虚数部分
    ·不可变数据类型
'''

#复数类型在科学计算中十分常见
x=123+456j
print('实数部分：',x.real)
print('虚数部分：',x.imag)


                                     #字符串类型（最常用的数据类型）
#字符串又被称为不可变的字符序列
#可以使用单引号、双引号、三引号或''' '''、""" """来定义
   #单引号和双引号定义的字符串必须在一行(分行报错)
str1='我不和任何人争，和任何人争我都不屑'
print(str1,type(str1))
str2="我不和任何人争，和任何人争我都不屑"
print(str2,type(str2))
#三引号定义的字符串可以分布在连续的多行
str3='''我不和任何人争，
和任何人争我都不屑'''
str4="""我不和任何人争，
和任何人争我都不屑"""
print(str3,type(str3))
print(str4,type(str4))

#字符串索引
s='HELLOWORLD'
print(s[0],s[-10])
print('北京欢迎你'[4])
print('北京欢迎你'[-1])

#字符串切片[N:M] -- 切片获取字符串中从N到M(不包含M)的子字符串
print(s[2:7])
print(s[-8:-3])
print(s[:5])#默认从0开始
print(s[0:])#默认到尾结束开始

#字符串拼接
x='2022年'
y='北京冬奥会'
print(x+y)
print(10*x) #x输出10次
print('北京' in y)#北京是否是y的子字符串
print('上海' in y)#上海是否是y的子字符串
