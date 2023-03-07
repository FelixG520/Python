# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！



intcount=[]
upstrcount=[]
lowstrcount=[]
othercount=[]
def number(a):
    for i in a:
        if i.isdigit():
            intcount.append(i)
        elif i.isupper():
            upstrcount.append(i)
        elif i.islower():
            lowstrcount.append(i)
        else:
            othercount.append(i)
    return intcount,upstrcount,lowstrcount,othercount
a=input('请输入一个字符串：')
a,b,c,d=number(a)
print('大写字母的个数：{}'.format(len(a)))
print('小写字母的个数：{}'.format(len(b)))
print('数字的个数：{}'.format(len(c)))
print('其他数字的个数：{}'.format(len(d)))
a=tuple(a)
b=tuple(b)
c=tuple(c)
d=tuple(d)
print(a,b,c,d)