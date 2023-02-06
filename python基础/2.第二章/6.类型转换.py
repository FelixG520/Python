# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
                                       #数据类型转换
#为什么要进行数据类型转换？
   #将不同数据类型的数据拼接在一起
'''

数据类型之间的转换-隐式类型转换
·通过数学运算可以隐式将int类型转成float类型
'''
a=10
b=3
print(a/b,type(a/b))
name='Felix'
age=18
print(type(name),type(age))#说明name与age的数据类型不同
#print('我叫'+name+'今年,'+age+'岁')#当str类型与int类型进行连接时，报错

# 解决方案：类型转换
print('我叫'+name+',今年'+str(age)+'岁')# + -->连接符

print('----------str()将其他类型转成str类型------------')
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

print('----------int()将其他类型转成int类型------------')
s1='128'
f1=98.7
s2='76.77'
ff=True
s3='hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))  #将str转成int类型，字符串为数字串
print(int(f1),type(int(f1)))  #将float转成int类型，截取整数部分，舍掉小数部分
#print(int(s2),type(int(s2))) #将str转成int类型，报错，因为字符串为小数串
print(int(ff),type(int(ff)))
#print(int(s3),type(int(s3))) #将str转成int类型时，字符串必须为数字串（整数），非数字串不允许转换，否则报错

print('----------float()将其他类型转成float类型------------')
s1='128.98'
s2='76'
ff=True
s3='hello'
i1=98
print(type(s1),type(s2),type(ff),type(s3),type(i1))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(ff),type(float(ff)))
#print(float(s3),type(float(s3)))   #字符串中的数据如果是非数字串，则不允许转换
print(float(i1),type(float(i1)))
