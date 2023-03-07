# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
1.什么叫模块_模块化编程的好处.编写程序文件
[root@master ~]# vi /opt/software/data/project/p_8/p_8.py
2.按i键进入编辑模式，输入以下代码
·Python len() 方法返回对象（字符、列表、元组等）长度或项目个数。
·Python ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
·Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.
·enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，
            一般用在 for 循环当中。Python 2.3. 以上版本可用，2.6 添加 start 参数。
·readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。如果碰到结束符 EOF 则返回空字符串
3.执行程序
[root@master ~]# cd /opt/software/data/project/p_8
[root@master p_8]# python3 p_8.py
4.ls查看是否生成文件
[root@master p_8]# ls
5.cat 查看生成文件的内容
[root@master p_8]#cat p_8_new.py
'''

#执行程序
filename = 'p_8.py'
with open(filename, 'r') as fp:
    lines = fp.readlines()
maxLength = len(max(lines, key=len))
lines = [line.rstrip().ljust(maxLength)+'#'+str(index)+'\n'for index, line in enumerate(lines)]
with open(filename[:-3]+'_new.py', 'w') as fp:
    fp.writelines(lines)
#ls查看是否生成文件
#cat 查看生成文件的内容