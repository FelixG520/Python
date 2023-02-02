# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

'''
·编码与解码的方式
    ·编码:将字符串转换为二进制数据(bytes)
    ·解码:将bvtes类型的数据转换成字符串类型
'''
#编码
s='天涯共此时'
print(s.encode(encoding='GBK'))    #在GBK这种编码格式中，一个中文占两个字节，输出结果中的b表示的是二进制
print(s.encode(encoding='UTF-8'))  #在UTF-8这种编码格式中，一个中文占三个字节，输出结果中的b表示的是二进制



#解码
#byte代表的就是一个二进制数据（字节类型的数据）
#用GBK编，就得用GBK解
byte=s.encode(encoding='GBK')       #编码
print(byte.decode(encoding='GBK'))  #解码
#print(byte.decode(encoding='UTF-8'))  UnicodeDecodeError: 'utf-8' codec can't decode byte 0xcc in position 0: invalid continuation byte


byte=s.encode(encoding='UTF-8')       #编码
print(byte.decode(encoding='UTF-8'))  #解码