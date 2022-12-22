# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！



def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)


#函数的调用
fun(10,20,30)   #函数调用时的参数传递，称为位置传参
lst=[11,22,33]

print('---------将序列中的每个元素都转换为位置实参，使用*-------------')
#fun(lst)   TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
fun(*lst)


print('---------将字典中的每个键值对都转换为关键字实参，使用**-------------')
fun(a=100,c=300,b=200)   #函数的调用，所以是关键字实参
dic={'a':111,'b':222,'c':333}
#fun(dic)   TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
fun(**dic)


def fun2(a,b=10):   #b是在在函数的定义处，所以b是形参，而且进行了赋值，所以b称为默认值形参
    print('a=',a)
    print('b=',b)

print('---------个数可变的位置形参---------')
def fun3(*args):  #个数可变的位置形参
    print(args)
fun3(10,20,30,40)

print('-------个数可变的关键字形参-----------')
def fun4(**args2):  #个数可变的关键字形参
    print(args2)
fun4(a=11,b=22,c=33,d=44,e=55)

print('--------关键字形参------------')
def fun5(a,b,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)
#调用fun5函数
fun5(10,20,30,40)          #位置实参传递
fun5(a=11,b=22,c=33,d=44)  #关键字实参传递
fun5(10,20,c=30,d=40)      #前两个参数采用的是位置实参传递，而c，d采用的是关键字实参传递


'''
需求:c,d只能采用关键字实参传递'''

print('-------------需求:c,d只能采用关键字实参传递-----------------')
def fun5(a,b,*,c,d):      #从*之后的参数，在函数调用时，只能采用关键字参数传递
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)
#调用fun5函数
#fun5(10,20,30,40)          #位置实参传递    #TypeError: fun5() takes 2 positional arguments but 4 were given
fun5(a=11,b=22,c=33,d=44)  #关键字实参传递
fun5(10,20,c=30,d=40)      #前两个参数采用的是位置实参传递，而c，d采用的是关键字实参传递



'''函数定义时的形参的顺序问题'''
def fun6(a,b,*,c,d,**args):
    pass

def fun7(*args,**args2):           #个数可变的位置形参放在个数可变的关键字形参之前
    pass

def fun8(a,b=10,*args,**args2):    #个数可变的位置形参放在个数可变的关键字形参之前
    pass

