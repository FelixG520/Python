# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


print(bool(0))     #False   0的布尔值为False
print(bool(8))     #True    非0的布尔值为Ture


#函数返回多个值时，结果为元组
def fun(num):
    odd=[]   #存奇数
    even=[]  #存偶数
    for i in num:
        if i%2:            #Ture为奇数，False为偶数
            odd.append(i)
        else:
            even.append(i)
    return odd,even      #结束时将odd和even返回


print('-------------函数的调用--------------')
lst=[10,29,34,23,44,53,55]
print(fun(lst))


'''函数的返回值可以有
    (1).如果函数没有返回值(函数执行完毕之后，不需要给调用处理提供数据)，return可以省略不写
    (2).函数的返回值，如果是1个，直接返回类型
    (3).函数的返回值，如果是多个，返回的结果为元组
    
    '''
print('----------------(1).如果函数没有返回值--------------------')
def fun1():
    print('hello')
    return     #return可以省略不写

fun1()

print('----------------(2).函数的返回值，如果是1个，直接返回类型--------------------')
def fun2():
    return 'hello'

res=fun2()
print(res)


print('----------------(3).函数的返回值，如果是多个，返回的结果为元组--------------------')
def fun3():
    return'hello','world'

print(fun3())



'''函数在定义时，是否需要写return，视情况而定'''