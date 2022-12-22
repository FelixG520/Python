# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
read([size]):从文件中读取size个字节或字符的内容返回。若省略[size],则读取到文件末尾,即一次读取文件所有内容
readline():从文本文件中读取一行内容
readlines():把文本文件中每一行都作为独立的字符串对象,并将这些对象放入列表返国
write(str):将字符串str内容写入文件
writelines(s_list):将字符串列表 s_list写入文本文件,不添加换行符
seek(offset[,whence]):把文件指针移动到新的位置,offset表示相对于whence的位置:
                      offset:为正,往结束方向移动;为负,往开始方向移动
                      whence不同的值代表不同含义:
                      0:从文件头开始计算(默认值)
                      1:从当前位置开如计算
                      2:从文件尾开始计算
tell():返回文件指针的当前位置
flush():把缓冲区的内容写入文件,但不关闭文件
close():把缓冲区的内容写入文件,同时关闭文件,释放文件对象相关
'''

#读
file=open('c.txt','r')
#print(file.read(2))   #读取两个字符，即“中国”
#print(file.readline()) #从文本文件中读取一行内容
print(file.readlines()) #把文本文件中每一行都作为独立的字符串对象,并将这些对象放入列表返会

#写
file.open('d.txt','a')
#file.write('hello')

file.close()