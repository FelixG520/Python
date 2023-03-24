#1、判断 101-200 之间有多少个素数，并输出所有素数。
from math import sqrt

for i in range(100,200):
    flag=1
    k=int(sqrt(i))
    for j in range(2,k+1):
        if i%j==0:
            flag=0
            break
    if flag==1:
        print(i,"是素数！")