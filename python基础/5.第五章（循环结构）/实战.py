#coding=utf-8
#判断是否是闰年
year=eval(input('请输入一个四位的年份：'))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,'年是闰年')
else:
    print(year,'年是平年')

'''
实战二
-题目:模拟10086查询功能
需求:输入1，显示当前余额;输入2，显示当前的剩余流量，单位为G;输入3，显示当前的剩余通话，单位为分钟:输入0,退出自助查询系统
'''

answer='y'
while answer=='y':
    print('------------------欢迎使用10086查询功能------------------------')
    print('1.查询当前余额')
    print('2.查询当前的剩余流量')
    print('3.查询当前剩余通话时长')
    print('0.退出系统')
    choice=input('请输入您要执行的操作:')
    if choice=='1':
        print('当前余额为：234.5元')
    elif choice == '2':
        print('当前的剩余流量为4GB')
    elif choice == '3':
        print('当前的剩余通话时长为200分钟')
    elif choice=='0':
        print('程序退出，谢谢您的使用！')
        break
    else:
        print('对不起您输入的有误，请重新输入！')
    answer=input('还要继续执行操作吗：y/n')
print('程序退出，谢谢您的使用！')


'''
实战四
-题目:猜数游戏
-需求:随机生成一个1~100之间的整数，然后用户循环猜这个数，
 对于用户的输入，可提示“大了”“小了”，直到猜准确为止，输出用户的猜测次数
'''
import random
rand=random.randint(1,100)
count=1 #记录猜的次数
while count<=10:
    number=eval(input('1-100请你猜一猜：'))
    if number==rand:
        print('猜对了！')
        break
    elif number>rand:
        print('大了')
    else:
        print('小了')
    count+=1
#判断次数
if count<=3:
    print('真聪明，一共猜了',count,'次')
elif count<=6:
    print('还可以，一共猜了',count,'次')
else:
    print('次数有点多啊，一共猜了',count,'次')
