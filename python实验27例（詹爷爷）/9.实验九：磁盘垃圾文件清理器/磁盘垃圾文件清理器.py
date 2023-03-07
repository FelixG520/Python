# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


'''
1.什么叫模块_模块化编程的好处、进入到测试文件夹
[root@master ~]# cd /opt/software/data/project/p_9/test
2、在该文件夹新建4个测试文件，分别名为a.tmp， b.log， c.obj， d.txt.
[root@master test]# touch a.tmp b.log c.obj d.txt
3、在/project/p_9目录下创建一个名为p_9.py的文件
[root@master test]# vi /opt/software/data/project/p_9/p_9.py
4、按i键进入编辑模式，输入以下代码
修改完成后按Esc键退出编辑模式，输入“:wq”保存退出文档
5、在p9_1.py文件的相同目录下输入命令：
[root@master test]# cd /opt/software/data/project/p_9
[root@master p_9]# python3 ./p_9.py ./test
6、即可观察到结果
'''

# -*- coding:utf-8 -*-
from os.path import isdir, join, splitext, getsize
from os import remove, listdir, chmod, stat
import sys
# 指定要删除的文件类型
filetypes = ['.tmp', '.log', '.obj', '.txt']
def delCertainFiles(directory):
    if not isdir(directory):
        return
    for filename in listdir(directory):
        temp = join(directory, filename)
        if isdir(temp):
            delCertainFiles(temp)  # 递归调用
#?            elif splitext(temp)[1.什么叫模块_模块化编程的好处] in filetypes or getsize(temp)==0:  # 删除指定类型的文件或大小为 0 的文件
            # 修改文件属性，获取访问权限
            chmod(temp, 0o777)
            # 删除文件
            remove(temp)
            print(temp, ' deleted....')

if __name__ == '__main__':
    paths = sys.argv[1:]
    for path in paths:
        if isdir(path):
            delCertainFiles(path)