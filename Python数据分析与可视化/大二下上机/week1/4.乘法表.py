print('-----------------九九乘法表------------------')
for i in range(1,10):               #行数
    for j in range(1,i+1):          #*数=所在行数
        print(i,'*',j,'=',i*j,end='\t')
    print()