# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''sqrt() 方法返回数字x的平方根
           注意：sqrt()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法
            import math
            math.sqrt()'''

import math
#输入底
bottom = input("输入底:")
#输入高
height = input("输入高:")
#将输入转换成浮点数形式
bottom = float(bottom)
height = float(height)
#计算斜边长
other = math.sqrt(bottom*bottom + height*height)    #math.sqrt()返回数字x的平方根
#输出
print("底:",bottom)
print("高:",height)
print("斜边:",other)
print(type(bottom),type(height),type(other))    #<class 'float'> <class 'float'> <class 'float'>



print('----------------个人实操-----------------')
import math
di=float(input('输入底:'))
gao=float(input('输入高:'))
xiebian=math.sqrt(di**2+gao**2)
print('底=',di,'\n高=',gao,'\n斜边=',xiebian)
print(type(di),type(gao),type(xiebian))         #<class 'float'> <class 'float'> <class 'float'>


print('----------------不变数据类型-----------------')
import math
di1= input("输入底:")
gao1 = input("输入高:")
xiebian1=math.sqrt(di**2+gao**2)
print('底=',di,'\n高=',gao,'\n斜边=',xiebian)
print(type(di1),type(gao1),type(xiebian1))      #<class 'str'> <class 'str'> <class 'float'>