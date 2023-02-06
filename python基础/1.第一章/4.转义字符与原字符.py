# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！
#转义字符
print('1.hello\nworld\n')#\     加转义字符首字母    n-->newline的首字母表示换行
print('2.hello\tworld')     #\t	水平制表符，也即 Tab 键，一般相当于四个空格
print('3.helloooo\tworld')
print('4.hello\rworld')#world把hello覆盖掉了     r-->return
print('5.hello\bworld')#\b是退一个格，将o退没了    b-->back
print('6.老师说：\'大家好\'')#print('老师说:'大家好'')报错



#不希望字符串中的转移字符起作用，就使用原字符，就是在字符串之前加上r或R
print(r'7.hello\nworld')
#注意事项，最后一个字符不能是\,但是\\行
#print(r'hello\nworld\')报错
print(r'8.hello\nworld\\')