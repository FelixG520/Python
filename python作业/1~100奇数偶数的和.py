
def sum():
    sum=0
    for i in range(1,101,2):
        sum=sum+i
    return sum
print(sum())



def sum():
    sum=0
    for i in range(2,101,2):
        sum=sum+i
    return sum
print(sum())
#2.编写程序，格式化输出杨辉三角
n=int(input("请输入杨辉三角的行数（n>1.什么叫模块_模块化编程的好处）："))
while(n<=1):
    n=int(input("请输入杨辉三角的行数（n>1.什么叫模块_模块化编程的好处）："))
triangle=[1,[1,1]]
for i in range(2,n):
   cur=[1]
   pre=triangle[i-1]
   for j in range(0,i-1):
       cur.append(pre[j]+pre[j+1])
   cur.append(1)
   triangle.append(cur)
print(str(triangle[0]).center(20))
for h in range(1,n):
    a=triangle[h]
    s=" "
    for k in range(0,h+1):
        s=s+str(a[k])+" "
    print(s.center(20))

#如果大的那个数，一旦他的倍数能整除小的那个数，就直接跳出循环，他的倍数就是最小公倍数



