# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


#字符串复制
str='Guangzhou'
print(str*3)            #str 3次复制   GuangzhouGuangzhouGuangzhou
print(3*str)            #str 3次复制   GuangzhouGuangzhouGuangzhou
print((str+' ')*3)      #Guangzhou Guangzhou Guangzhou
'''print(str*str)         TypeError: can't multiply sequence by non-int of type 'str'
                                      复制操作只能1个字符串和1个整数，其他任何类型组合均会报错'''
