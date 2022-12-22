# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！



#二重循环中的break和continue只用于控制本层循环




print('------------break--------------')
for i in range(5):       #代表外层循环要执行5次
    for j in range(1,11):
        if j%2==0:
            break    #跳出循环
        print(j)


print('顺便观察换行跟不换行的区别于格式')
#不换行
print('-------------continue-----------------')
for i in range(5):  # 代表外层循环要执行5次
    for j in range(1, 11):
        if j % 2 == 0:
            continue  #继续循环
        print(j)




#换行
print('-------------continue-----------------')
for i in range(5):  # 代表外层循环要执行5次
    for j in range(1, 11):
        if j % 2 == 0:
            continue  #Ture，继续循环;False，换行
        print(j,end=('\t'))
    print()




'''************************
外层循环执行一次，内层要执行完整的一轮，最好最多不要超过三层'''
