# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''·函数定义默认值参数
     ·函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参

     '''

def fun(a,b=10):    #b称为默认值参数
    print(a,b)

print('------------函数的调用---------------')
fun(100)   #只传一个参数，b采用默认值
fun(20,30) #30将默认值10替换


print('hello')            #按住ctrl点print可查看print的默认值
print('world')            #end默认换行

print('hello',end='\t')   #修改了end的默认值
print('world')