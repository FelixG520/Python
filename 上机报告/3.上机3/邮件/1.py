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
