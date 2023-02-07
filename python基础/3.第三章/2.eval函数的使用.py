'''
·eval()函数
  - eval(s)函数将去掉字符串s最外侧的引号，并按照Python语句方式执行去掉引号后的字符串
  - 语法格式
              变量=eval(字符串)
  - eval()函数经常和input()函数一起使用，用来获取用户输入的数值型
'''


s='3.14+3'
print(s,type(s))
x=eval(s)   #去引号，执行了加法运算
print(x,type(x))


#  - eval()函数经常和input()函数一起使用，用来获取用户输入的数值型
age=eval(input('请输入您的年龄：'))  #将字符类型转成了int类型，相当于int(age)
print(age,type(age))
height=eval(input('请输入您的身高：'))  ##将字符类型转成了float类型，相当于float(height)
print(height,type(height))

hello='北京欢迎你'
print(hello)
print(eval('hello'))

num=eval(input('请输入一个4位数：'))
sd=num%10
tens=num//10%10
hun=num//100%10
tho=num//1000
print('个位上的数字是：',sd)
print('十位上的数字是：',tens)
print('百位上的数字是：',hun)
print('千位上的数字是：',tho)

