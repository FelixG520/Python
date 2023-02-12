# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
·判断字符串的方法
    ·isidentifier()  判断指定的字符串是不是合法的标识符(字母、数字、下划线)
    ·isspace()       判断指定的字符串是否全部由空白字符组成(回车、换行、水平制表符)
    ·isalpha()       判断指定的字符串是否全部由字母组成
    ·isdecimal()     判断指定字符串是否全部由十进制的数字组成
    ·isnumeric()     判断指定的字符串是否全部由数字组成
    ·isalnum()       判断指定字符串是否全部由字母和数字组成
'''



s='hello,python'
print('-------------isidentifier()  判断指定的字符串是不是合法的标识符-------------------')
#合法的标识符(字母、数字、下划线)
print('1.',s.isidentifier())          #False     ','不是合法的标识符
print('2.','hello'.isidentifier())    #True
print('3.','张三_'.isidentifier())     #True
print('4.','张三_123'.isidentifier())  #True



print('---------------isspace()  判断指定的字符串是否全部由空白字符组成(回车、换行、水平制表符)---------------')
print('5.','\t'.isspace())    #Ture


print('------------isalpha()   判断指定的字符串是否全部由字母组成-----------------')
print('6.','abc'.isalpha())     #Ture
print('7.','张三'.isalpha())     #Ture
print('8.','张三1'.isalpha())    #False     '1‘不是字母


print('------------isdecimal()  判断指定字符串是否全部由十进制的数字组成------------------')
print('9.','123'.isdecimal())       #Ture
print('10.','123四'.isdecimal())     #False
print('11.','ⅡⅡⅡ'.isdecimal())     #False  Ⅱ罗马数字不是十进制


print('----------isnumeric()  判断指定的字符串是否全部由数字组成------------')
print('12.','123'.isnumeric())   #Ture
print('13.','123四'.isnumeric())  #True    ‘四’也是数字
print('14.','ⅡⅡⅡ'.isnumeric())  #Ture  罗马数字也是数字



print('---------------isalnum()  判断指定字符串是否全部由字母和数字组成------------------')
print('15.','abc1'.isalnum())    #Ture
print('16.','张三123'.isalnum())  #Ture
print('17.','abc!'.isalnum())    #False    '!'不属于字母和数字

print('Helloworld'.islower())  #判断是不是都是小写字母
print('helloworld'.islower())  #判断是不是都是小写字母
print('hello你好'.islower())

print('Helloworld'.isupper()) #判断是不是都是大写字母
print('HELLOWORLD'.isupper()) #判断是不是都是大写字母
print('HELLO你好'.isupper())

print('Hello'.istitle()) #判断是否首字母大写

print('\t'.isspace()) #判断是否都是空白字符
print('   '.isspace()) #判断是否都是空白字符





print(s.startswith('h'))#是否以H开头
print(s.startswith('P'))#是否以P开头
print('demo.py'.endswith('.py'))
print('demo.txt'.endswith('.txt'))
