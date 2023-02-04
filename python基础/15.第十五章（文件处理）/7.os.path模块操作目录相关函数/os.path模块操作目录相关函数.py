'''

abspath(path):用于获取文件或目录的绝对路径
exists(path):用于判断文件或目录是否存在，如果存在返回True，否则返回False
join(path, name):将目录与目录或者文件名拼接起来
split():从一个目录中提取文件名和路径
splitext():分离文件名和扩展名
basename(path):从一个目录中提取文件名
dirname(path):从一个路径中提取文件路径，不包括文件名
isdir(path):用于判断是否为路径

'''

import os.path
print(os.path.abspath('python基础'))     #abspath(path):用于获取文件或目录的绝对路径

print(os.path.exists('text1'),os.path.exists('text'))      #exists(path):用于判断文件或目录是否存在，如果存在返回True，否则返回False

print(os.path.join('text1','text2'))     #join(path, name):将目录与目录或者文件名拼接起来

print(os.path.split('E:\高帆的python\python基础\\15.第十五章（文件处理）\\text.csv'))

print(os.path.splitext('text.csv'))       #splitext():分离文件名和扩展名

print(os.path.basename('E:\高帆的python\python基础\\15.第十五章（文件处理）\\text.csv'))    #basename(path):从一个目录中提取文件名

print(os.path.dirname('E:\高帆的python\python基础\\15.第十五章（文件处理）'))    #dirname(path):从一个路径中提取文件路径，不包括文件名

print(os.path.isdir('E:\高帆的python\python基础\\15.第十五章（文件处理）'))     #isdir(path):用于判断是否为路径
