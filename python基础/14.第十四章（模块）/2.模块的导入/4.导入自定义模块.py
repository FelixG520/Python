# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


#在此python文件中导入calc自定义模块使用
import calc     #右键文件夹，点击Mark Directory as
print(calc.add(10, 20))
print(calc.div(10, 4))


from calc import add
print(add(10,20))