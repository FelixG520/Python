# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
                          #continue语句
#·用于结束当前循环，进入下一次循环，通常与分支结构if一起使用（后面有多少代码不管了，从头再来）


'''使用continue语句实现
   输出1到50之间的所以5的倍数（和5的余数为0）
   什么样的数不是5的倍数？与5的余数不为0的数都不是5的倍数
   '''
for item in range(1,51):
    if item%5==0:
        print(item)


print('------------使用continue-----------------')
for item in range(1,51):
    if item%5!=0:    #也可以用 if item%5:
        continue#如果满足条件跳出循环
    print(item)


for item in range(1,51):
    if item%5!=0:    #也可以用 if item%5:
        continue#如果满足条件跳出循环
    else:
        print(item)