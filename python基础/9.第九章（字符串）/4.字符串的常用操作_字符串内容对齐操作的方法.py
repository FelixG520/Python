# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
·字符串内容对齐操作的方法
    ·center()居中对齐,第1个参数指定宽度,第2个参数指定填充符,第2个参数是可选的,默认是空格,如果设置宽度小于实际宽度则刈眶回原字符串
    ·ljust()左对齐,第1个参数指定宽度,第2个参数指定填充符,第2个參数是可选的,默认是空格如果设置宽度小于实际宽度则返回原字符串
    ·rjust()右对齐,第1个参数指定宽度,第2个参数指定填充符,第2个参数是可选的，默认是空格如果设置宽度小于实际宽度则返回原字符串
    ·zfill()右对齐，左边用0填充,该方法只接收一个参数,用于指定字符串的宽度,如果指定的宽度小于等于字符串的长度,返回字符串本身
'''


s='hello,python'
#居中
print(s.center(20,'*'))    #12个字符，给的宽度是20，因此左右两边各填充(20-12)/2=4个字符
print(s.center(20))
#左对齐
print(s.ljust(20,'*'))     #只填充右侧
print(s.ljust(20))
#右对齐
print(s.rjust(20,'*'))     #只填充左侧
print(s.rjust(20))
#填充符不写默认填充空格
print(s.center(20))
print(s.ljust(20))
print(s.rjust(20))



print('--------------------如果设置宽度小于实际宽度则返回回原字符串------------------------')
print(s.center(10,'*'))
print(s.ljust(11,'*'))
print(s.rjust(9,'*'))



print('---------------右对齐，使用0进行填充----------------------')
print(s.zfill(20))
print(s.zfill(10))
print('-8910'.zfill(8))        #把0添到‘-’之后，算上‘-’总共四个字符，因此添了3个0
