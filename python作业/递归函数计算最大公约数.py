# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！



def find_divisor(a,b):
    if a<b:
        a,b=b,a
    if a%b==0:
        return b
    else:
        return find_divisor(b,a%b)
print(find_divisor(88,24))
