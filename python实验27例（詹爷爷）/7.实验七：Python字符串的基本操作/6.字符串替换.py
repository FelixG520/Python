# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


s='one, two and three'
s1='one,\ttwo\tand\tthree'    #\t	水平制表符，也即Tab键，一般相当于四个空格
print(s)                       #one, two and three
print(s.replace('one','1.什么叫模块_模块化编程的好处'))    #1.什么叫模块_模块化编程的好处, two and three         将字符串s中的每个’one’替换为'1.什么叫模块_模块化编程的好处'
print(s.replace('one',' '))    # , two and three         将字符串s中的每个’one’替换为' '
print(s1)                      #one, 	two	and	three
print(s1.expandtabs(8))        #one,    two     and     three        将字符串s中制表符扩展为空格，宽度为8
print(s1.expandtabs(10))       #one,      two       and       three  将字符串s中制表符扩展为空格，宽度为10