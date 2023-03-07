# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''1.什么叫模块_模块化编程的好处、要求：写出答案，再在Python编译器上运行验证。
（1.什么叫模块_模块化编程的好处）进制转换,把以下进制转换成十进制：
0xABC=2748
0o7653=4011
0b11101010111101=15037
'''
print('（1.什么叫模块_模块化编程的好处）进制转换,把以下进制转换成十进制：')
print(0xABC)
print(0o7653)
print(0b11101010111101)


'''
(2）数值转换：
a=10,b=3,a/b=3,原因是什么10除以3商3
a=10.0,b=3,a/b=3.33333333333335,原因是什么浮点数与整数相除等于浮点数'''
print('(2）数值转换：')
a=10
b=3
print(a/b)
a=10.0
b=3
print(a/b)

'''在Python中，整数的取值范围是：32位系统:2^31-1.什么叫模块_模块化编程的好处,64位系统：2^63-1.什么叫模块_模块化编程的好处，其后进入高精度计算'''

'''0.00045的科学记数法是'''
print('0.00045的科学记数法是')
print(4.5e-4)

'''a=5.5,int(a)=5,b=5.3,int(b)=5'''
print('a=5.5,int(a)=5,b=5.3,int(b)=5')
a=5.5
print(int(a))
b=5.3
print(int(b))

'''虚数c=4+3j,type(c)=<type‘complex’>，c.real=4.0,c.imag=3.0'''
print('虚数c=4+3j,type(c)=<type‘complex’>，c.real=4.0,c.imag=3.0')
c=4+3j
print(type(c))
print(c.real)
print(c.imag)

'''d=10,float(d)=10.0,f=3.5,complex(f)=(3.5+0j)
g=3+4j,float(g)结果是什么TypeError: can't convert complex to float(错误，无法转换浮点数和复数)'''
d=10
print(float(d))
f=3.5
print(complex(f))
g=3+4j
#print(float(g))   TypeError: can't convert complex to float(错误，无法转换浮点数和复数)



'''·（3）数值计算：
a=10,b=4,d=10求下面的结果:
a+b=14,a-b=6,a*b=40,a/d=1.什么叫模块_模块化编程的好处.0,a//b=2,a%b=2,
divmod(a,b)=(2, 2),pow(a,b)=10000,a**b=10000'''
a=10
b=4
d=10
print(a+b,a-b,a*b,a/d,a//b,a%b,
      divmod(a,b),pow(a,b),a**b)
'''
c=20,d=5,5cd结果是什么SyntaxError: invalid syntax，为什么:5cd相当于变量，5*c*d才是表达式'''
c=20
d=5
#print(5cd)   错误，5cd相当于变量，5*c*d才是表达式



