# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
1.什么叫模块_模块化编程的好处.新建测试文档dream.txt,
[root@master ~]# vi /opt/software/data/project/p_16/dream.txt
2.按i键进入编辑模式，在里面任意输入几个单词，完成后按Esc键退出编辑模式，输入“：wq”保存退出
3.编写程序文件，输入参考代码
[root@master ~]# vi /opt/software/data/project/p_16/p_16.py
4.按i键进入编辑模式，输入以下代码
按Esc键退出编辑模式，输入“:wq”保存退出
5.执行程序文件
[root@master ~]# cd /opt/software/data/project/p_16
[root@master p_16]# python3 /opt/software/data/project/p_16/p_16.py
'''



#encoding=utf-8
import string
speach=[]       #演讲列表
count=0         #统计列表的长度
purSpeach=[]    #纯单词列表
unique=[]
sentence=open("dream.txt","r") #打开文件
for words in sentence:
    temp = words.split()       # temp为临时列表,注意以空格分隔单词
    speach.extend(temp)        # 列表汇总
count = len(speach)

# 对文本中的单词进行预处理，把纯单词加入新列表。
for word in speach:
    newWord = ""
    for char in word:
        if char not in string.punctuation:
            newWord += char
    purSpeach.append(newWord)

count=len(purSpeach)
print(purSpeach)
print('文件长度为:%d'%count)

#获取不重复单词
for word in purSpeach:
    word = word.lower()
    if word not in unique:
        unique.append(word)

#打印不重复单词
for word in unique:
    count += 1
    print(word, end=' ')
print("\n不重复的单词个数为:",len(unique))


