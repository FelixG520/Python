# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
1.什么叫模块_模块化编程的好处.新建测试文档,两个测试txt文档都输入: Hello
[root@master ~]# vi /opt/software/data/project/p_12/test/test1.txt
按i键进入编辑模式输入内容Hello,按Esc键退出编辑模式，输入“:wq”保存退出
[root@master ~]# vi /opt/software/data/project/p_12/test/test2.txt
按i键进入编辑模式输入内容Hello,按Esc键退出编辑模式，输入“:wq”保存退出
2.编写程序文件
[root@master ~]# vi /opt/software/data/project/p_12/p_12.py
3.按i键进入编辑模式，输入以下代码
4.执行程序文件
[root@master ~]# cd /opt/software/data/project/p_12/test
[root@master test]# python3 ../p_12.py
当程序提示what are you looking for?，输入“Hello”
'''



import os
def check(searchStr, count, fileList, dirList):
    for dirName, dirs, files in os.walk("."):
        for f in files:
            if os.path.split(f)[1].split(".")[1] == "txt":
                count = count + 1
                aFile = open(os.path.join(dirName, f), "r")
                fileStr = aFile.read()
                if searchStr in fileStr:
                    fileName = os.path.join(dirName, f)
                    fileList.append(fileName)
                if dirName not in dirList:
                    dirList.append(dirName)
                    aFile.close()
    return count
print(os.getcwd())
theStr=input("what are you looking for? ")
fileList=[]
dirList=[]
count=0
count=check(theStr,count,fileList,dirList)
print("looked at %d text files"%(count))
print("found %d directories containing text files"%(len(dirList)))
print("found %d files containing string :%s"%(len(fileList),theStr))
print("\n****Direcotries List****")
for dirs in dirList:
    print(dirs)
print("\n****File List*****")
for f in fileList:
    print(os.path.split(f)[1])