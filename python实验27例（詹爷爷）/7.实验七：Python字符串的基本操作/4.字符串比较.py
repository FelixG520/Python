# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！



#字符串比较
#比较原理:两上字符进行比较时,比较的是其ordinal value(原始值)，调用内置函数ord可以得到指定字符的ordinal value
print('a'=='a')   #True  两个字符相同，返回真
print('a'=='A')   #False 两个字符不相同，返回假


print(ord('a'),ord('A'))
print('a'!='A')   #True   ord('a')=97，ord('A')=65，97!=65返回真
print('a'>'A')    #True   ord('a')=97，ord('A')=65，97>65返回真

print('1.什么叫模块_模块化编程的好处'<'2')    #True

str="How are you"
print(str.startswith("How"))    #True 比较str的开头部分”How”

str="How are you"
print(str.endswith("you",6))           #True
print(str.endswith("you",6,10))        #False
print(str.endswith("you",6,len(str)))  #True
