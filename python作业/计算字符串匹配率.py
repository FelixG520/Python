# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


def rate(orgin,userinput):
    if not(isinstance(orgin,str) and isinstance(userinput,str)):
        print('The two parameters must be string')
        return
    if len(orgin)<len(userinput):
        print('sorry')
        return
    right =0
    for orgin_char,user_char in zip(orgin,userinput):
        if orgin_char == user_char:
            right +=1
    return right/len(orgin)
a = 'have a nice day'
b = 'Have a good Day'
print(rate(a,b))
