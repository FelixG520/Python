# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


#字符串格式化输出
import math
print(math.pi)                       #未指定精度
print('-------------使用%表示宽度和精度---------------')
print('pi is'+'%.2f' %(math.pi))       #%.2f     总宽度为0，小数点后2位
print('Pi is'+'%8.2f' %(math.pi))      #%8.2f    总宽度为8，小数点后2位
print('Pi is'+'%8.4f' %(math.pi))      #%8.4f    总宽度为8，小数点后4位