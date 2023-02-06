'''
.Python是一种解释类型的编程语言
.Python解释器在语法上不支持白然语言编程方式
'''
print('helloworld')
print(520)
print(3+1)


#根据ASCII码输出
print('b')   #输出字符b
print(chr(98))

#c通过ASCII显示字符，使用内置函数chr()
print('C')
print(chr(67))

print(8)   #输出字符8
print(chr(56))


'''
Python3.0以Unicode为内部字符编码。Unicode采用双字节16位来进行编号，
可编65536个字符，采用十六进制4位表示一个编码
'''
print(ord('北'))   #这个数字的编码 -- 21271 -- 十六进制为5317
print('\u5317')
print('\u5317\u4eac')

#输出到文件
fp=open('note.txt','w') #打开文件  w-->write
print('北京欢迎你',file=fp) #输出到文件中
fp.close() #关闭文件