# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
常用的文件打开模式
·文件的类型
   ·按文件中数据的组织形式,文件分为以下两大类
     ·文本文件:存储的是普通“字节”文本,默认为unicode字符集,可以使用记本事程序打开
     ·二进制文件:把数据内容用“字节”进行存储,无法用记事本打开,必须使用专用的软件打开,举例:mp3音频文件jpg图片doc文档等
打开模式：
r:以只读模式打开文件,文件的指针将会依在文件的所员
w:以只写模式打开文件,如果文件不存在则创建,如果文件存在,则覆盖原有内容,文件指针在文件的开头
a:以追加模式打开文件,如果文件不存在则创建,文件指针在文件开头,如果文件存在,则在文件末尾追加内容,文件指针在原文件末尾
b:以二进制方式打开文件,不能单独使用,需要与共它模式一起使用,rb,或者wb
+:以读写方式打开文件,不能单独使用,需要与其它模式一起使用,a+
'''


#w:以只写模式打开文件,如果文件不存在则创建,如果文件存在,则覆盖原有内容,文件指针在文件的开头
file=open('b.txt','w')
file.write('Python')
file.close()

#a:以追加模式打开文件,如果文件不存在则创建,文件指针在文件开头,如果文件存在,则在文件末尾追加内容,文件指针在原文件末尾
file=open('b.txt','a')
file.write('Python')
file.close()

#b:以二进制方式打开文件,不能单独使用,需要与共它模式一起使用,rb,或者wb
src_file=open('毕业合影.jpg','rb')
target_file=open('copy毕业合影.jpg','wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()