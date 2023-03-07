#代码用于实现两个整数间的最小公倍数算法：


def fangfa(a,b):
    if a>b:
        bigger=a
        smaller=b
    else:
        bigger=b
        smaller=a
    i=1
    while True:
        if (bigger*i)%smaller==0:                     #如果大的那个数，一旦他的倍数能整除小的那个数，就直接跳出循环，他的倍数就是最小公倍数
            print('最小公倍数为：',(bigger*i))
            break
        i+=1


if __name__ == '__main__':
    a = int(input('请输入第一个数：'))
    b = int(input('请输入第二个数：'))
    fangfa(a,b)




#该函数返回两个整数的最大公约数""


def fangfa(a,b):
    if a>b:
        smaller=b
    else:
        smaller=a
    y=1   #给出一个默认值
    for i in range(1,smaller+1):           #range函数左闭右开
        if (a%i==0) and (b%i==0):      #如果是公约数，y等于公约数；然后如果再找到一个更大的公约数，y被更大公约数覆盖
            y=i
            # break                      #如果加break就是遇到最小的公约数就跳出循环，展示出最小公约数
    print('最大公约数为：',y)



if __name__ == '__main__':
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    fangfa(a,b)





