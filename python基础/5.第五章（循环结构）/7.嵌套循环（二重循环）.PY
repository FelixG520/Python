 # 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

                           #嵌套循环
#·循环结构中又嵌套了另外的完整的循环结构，其中内层循环作为外层循环的循环体执行




'''输出一个三行四列的矩形'''
for i in range(1,4):                #行数，执行三次，一次是一行
    for j in range(1,5):
        print('*',end='\t')         #不换行输出（end是将结果输到同一行，\t是四个空字符）
    print()                         #换行


'''九九乘法表直角三角形'''
for i in range(1,10):               #行数
    for j in range(1,i+1):          #*数=所在行数
        print('*',end='')           #不用\t即*与*之间不空字符
    print()


print('-----------------九九乘法表------------------')
for i in range(1,10):               #行数
    for j in range(1,i+1):          #*数=所在行数
        print(i,'*',j,'=',i*j,end='\t')
    print()

#三行四列矩形
print('-----------------三行四列矩形------------------')
for i in range(1,4):
    for j in range(1,5):
        print('*',end='')
    #换行
    print()

#等腰直角三角形
print('-----------------等腰直角三角形------------------')
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()


#倒等腰直角三角形
print('-----------------倒等腰直角三角形------------------')
for i in range(1,6):
    for j in range(1,6-i+1):
        print('*',end='')
    print()

#等腰三角形
print('-----------------等腰三角形------------------')
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
    print()

#菱形
print('-----------------菱形-----------------')
row=eval(input('请输入菱形的行数'))
top_row=(row+1)//2  #上半部分的行数
#上半部分
for i in range(1,top_row+1):
    for j in range(1,top_row+1-i):
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
    print()
#下半部分
bottom_row=row//2
for i in range(1,bottom_row+1):
    #直角三角形
    for j in range(1,i+1):
        print(' ',end='')
    #倒三角形
    for k in range(1,2*(bottom_row-i+1)):
        print('*',end='')
    print()


#空心菱形
print('-----------------空心菱形-----------------')
row=eval(input('请输入菱形的行数'))
top_row=(row+1)//2  #上半部分的行数
#上半部分
for i in range(1,top_row+1):
    for j in range(1,top_row+1-i):
        print(' ',end='')
    for k in range(1,i*2):
        if k==1 or k==i*2-1:
            print('*', end='')
        else:
            print(' ',end='')
    print()
#下半部分
bottom_row=row//2
for i in range(1,bottom_row+1):
    #直角三角形
    for j in range(1,i+1):
        print(' ',end='')
    #倒三角形
    for k in range(1,2*(bottom_row-i+1)):
        if k==1 or k==2*(bottom_row-i+1)-1:
            print('*', end='')
        else:
            print(' ',end='')
    print()

