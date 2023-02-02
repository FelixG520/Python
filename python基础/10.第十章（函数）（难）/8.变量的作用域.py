# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
·变量的作用域
   ·编程代码能访问该变量的区域
   ·根据变量的有效范围可分为
     ·局部变量
        ·在函数内定义并使用的变量,只在函数内部有效,局部变量使用 global 声明,这个变量就会称全局变量
     ·全局变量
        ·函数体外定义的变量,可作用于函数内外'''




def fun(a,b):
    c=a+b     #c就称为局部变量，因为c是在函数体内进行定义的变量；a，b为函数的形参，作用范围也是函数内部，相当于局部变量
    print(c)

#print(c)   NameError: name 'c' is not defined   因为a和c超出了起作用的范围（超出了作用域）
#print(a)   NameError: name 'a' is not defined


name='张三'     #name的作用范围为函数内部和外部都可以使用，称为全局变量
print(name)

def fun2():
    print(name)
#调用函数
fun2()

def fun3():
    global age   #函数内部定义的变量，局部变量，局部变量使用global声明，这个变量实际上就变成了全局变量
    age=20
    print(age)
fun3()
print(age)