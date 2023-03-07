# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


#编写程序，输入整数n(n≥0)，分别利用for循环和while循环求n!
n=int(input("输入一个正整数:"))
sum=1
for i in range(1,n+1):
    sum=sum*i
print(sum)

n=int(input("请输入一个正整数"))
sum=1
i=1
while(i<=n):
    sum=sum*i
    i=i+1
print(sum)



