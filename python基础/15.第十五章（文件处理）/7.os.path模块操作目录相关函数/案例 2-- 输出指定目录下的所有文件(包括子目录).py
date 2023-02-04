
import os
path=os.getcwd()
lst_files=os.walk(path)
print(lst_files)#generator object -- 迭代器对象，可以遍历查看,返回元组

for dirpath,dirname,filename in lst_files:
    '''
    print(dirpath)
    print(dirname)
    print(filename)
    print('-------------------------------------------------------------')'''
    for dir in dirname:
        print(os.path.join(dirpath,dir)) #当前目录下有多少子目录
    print('----------------------------------------------------')
    for file in filename:
        print(os.path.join(dirpath,file))
    print('----------------------------------------------------')
