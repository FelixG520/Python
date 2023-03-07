# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


import random
Cave = [1,2,3,4,5]
fox = random.randint(0,4)
while(True):
    choice = int(input('这里有五个洞口1~5，请输入小狐狸所在洞口:'))
    if choice == Cave[fox]:
        print('恭喜你抓到小狐狸了！')
        break
    else:
        print('很遗憾!')
    if 0 <= fox < 4:
        fox += 1
    else:
        fox -= 1
    continue
