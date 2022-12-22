# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


'''
·字符串的其他操作
   ·字符串替换
     ·replace()   第1个参数指定被替换的子串,第2个参数指定替换子串的字符串,该方法返回替換后得到的字符串,替换前的字符串不发生变化,
                  调用该方法时可以通过第3个参数指定最大替换次数
·字符串的合并
   ·join()   将列表或元组中的字符串合并成一个字符串
'''


s='hello,Python'
print(s.replace('Python','Java'))      #用Java替换了Python     hello,Java
s1='hello,Python,Python,Python'
print(s1.replace('Python','Java',2))   #用Java换Python两次     hello,Java,Java,Python


lst=['hello','Java','Python']
print('|'.join(lst))
print(''.join(lst))


t=('hello','Java','Python')
print(''.join(t))


print('*'.join('Python'))    #P*y*t*h*o*n