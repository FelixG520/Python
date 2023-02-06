# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

#变量是内存中一个带变量的盒子，把需要的数据放进去
name='Felix'
print(name)
'''变量由三部分组成
 ·标识：表示对象所存储的内存地址，使用内置函数id（obj）来获取
 ·类型：表示的是对象的数据类型，使用内置函数type（obj）来获取
 ·值：表示对象所存储的具体数据，使用print（obj）可以将值进行打印输出'''
print('标识:',id(name))
print('类型:',type(name))
print('值:',name)


'''
- Python是一种动态类型的语言，变量的类型可以随时变化
    ·使用内置函数type()可以查看变量的数据类型
- 允许多个变量指向同一个值
    ·使用内置函数id()可以返回变量所指的内存地址
'''
my_name='zhangsan'
luck_number=6
print(my_name,'的幸运数字为',luck_number)
print('luck_number的数据类型是：',type(luck_number))

#变量的值可以更改
luck_number='123456789'
print('luck_number的数据类型是：',type(luck_number))

#多个变量指向同一个值
no=number=1024
print(no,number)
print(id(no))
print(id(number))

'''
变量的定义及使用
·变量命名应遵循以下几条规则
- 变量名必须是一个有效的标识符
- 变量名不能使用Pvthon中的保留字
- 慎用小写字母I和大写字母O
- 应选择有意义的单词作为变量名
·常量
- 常量就是在程序运行过程中，值不能改变的量
- Python中没有定义常量的保留字
- 常量规定使用大写字母和下划线组成
- 常量首次赋值后，还是可以被其他代码修改的
'''
