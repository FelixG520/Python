'''
目录操作
    ·os模块是Python内置的与操作系统功能和文件系统相关的模块该模块中的语句的执行结果通常与操作系统有关，
    在不同的操作系统上运行，得到的结果可能不一样。
    ·os模块与os.path模块用于对目录或文件进行操作

os模块操作目录相关函数
getcwd():返回当前的工作目录
listdir(path):返回指定路径下的文件和目录信息
mkdir(path[,model):创建目录
makedirs(pathl/path2... [, mode]):创建多级目录
rmdir(path):删除目录
removedirs(path1/path2......):删除多级目录
chdir(path):将path设置为当前工作目录

'''

import os
print(os.getcwd())   #getcwd():返回当前的工作目录

lst=os.listdir('../6.os模块的常用函数')   #listdir(path):返回指定路径下的文件和目录信息
print(lst)


#os.mkdir('textdir')     #mkdir(path[,model):创建目录

#os.makedirs('A/B/C/D/E')     #makedirs(pathl/path2... [, mode]):创建多级目录

#os.rmdir('textdir')     #rmdir(path):删除目录

#os.removedirs('A/B/C/D/E')      #removedirs(path1/path2......):删除多级目录

os.chdir('E:\\高帆的python\python基础\\15.第十五章（文件处理）\\5.with语句')      #chdir(path):将path设置为当前工作目录
print(os.getcwd())
os.chdir('E:\\高帆的python\python基础\\15.第十五章（文件处理）\\6.os模块的常用函数')      #chdir(path):将path设置为当前工作目录
print(os.getcwd())