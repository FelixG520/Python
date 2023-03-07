# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！






st=input('请输入一串字符串：')
print(st)                                               #输出用户输入的字符串
my_list0=list(st)                                       #将字符串转换成列表
my_list1=[]                                             #定义空列表
for i in range(len(my_list0)):
    if my_list0[i]!='i':
        my_list1.append(my_list0[i])                    #将不是i的复制到新列表my_list1中
    else:
        my_list1.append(my_list0[i].upper())            #将i转换成I，并放到新列表my_list1中
print(''.join(my_list1))                                #将列表转换成字符串并输出

