'''
Python程序设计上机3

练习：字符串的设计与应用
注意：要求把源代码和运行结果按上机报告的要求贴在报告里

目的：
1、熟练字符串的设计与应用编程。
2、理解字符串函数。
内容：
1、编写程序，首先检查输入的一个密码字符串pwd是否至少是8位且含有字母，并判断密码字符串的安全强度。
强度判断标准：分别统计是否包含数字和小写字母、大写字母、标点符号。
参考代码如下：（但是该程序稳定性不好，需要自己去改进）
import string
def check(pwd):
    #密码必须含有字母，且长度至少为8位
    #import re
    if len(pwd)<8:
        return 'not suitable for password'
    if pwd.isdigit():
        return 'not suitable for password'
    #密码强度等级与包含字符种类的对应关系
    d={1:'bellow middle',2:'above middle',3:'strong'}
    #分别用来标记pwd是否含有数字和小写字母、大写字母、标点符号
    r=[False]*3

    for ch in pwd:
        #是否包含小写字母
        if not r[0] and ch in string.ascii_lowercase:
            r[0]=True
        #是否包含大写字母
        elif not r[1] and ch in string.ascii_uppercase:
            r[1]=True
        #是否包含标点字母
        elif not r[2] and ch in string.punctuation:
            r[2]=True
    #统计包含的字符种类，返回密码强度
    return d.get(r.count(True),'error')
passwd=input('输入密码：')
print(check(passwd))


'''
import string
import re


def check(pwd):
    # 密码必须含有字母，且长度至少为8位
    if len(pwd) < 8:
        return 'not suitable for password'
    else:
        pattern = re.compile('r','(?=.{8,})(?=.*\d{1,})(?=.*[A-Z]{1,}|(?=.*[a-z]{1,})')
    index = 0
    while True:
        Result = pattern.search(pwd, index)
        if Result:
            break
        return 'not suitable for password'

    # 密码强度等级与包含字符种类的对应关系
    d = {1: 'bellow middle', 2: 'above middle', 3: 'strong'}
    # 分别用来标记pwd是否含有数字和小写字母、大写字母、标点符号
    r = [False] * 3

    for ch in pwd:
        # 是否包含小写字母
        if not r[0] and ch in string.ascii_lowercase:
            r[0] = True
        # 是否包含大写字母
        elif not r[1] and ch in string.ascii_uppercase:
            r[1] = True
        # 是否包含标点字母
        elif not r[2] and ch in string.punctuation:
            r[2] = True
    # 统计包含的字符种类，返回密码强度
    return d.get(r.count(True), 'error')


passwd = input('输入密码：')
print(check(passwd))