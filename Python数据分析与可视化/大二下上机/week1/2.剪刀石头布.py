#coding=utf-8
import random
player_score=0
computer_score=0
print('''
********************************************************
                  石头    剪刀     布
********************************************************
''')

player_name=input('请输入玩家姓名：')
print('1.貂蝉   2.曹操   3.诸葛亮')
choice=eval(input('请输入电脑角色：'))
if choice==1:
    computer_name='貂蝉'
elif choice==2:
    computer_name='曹操'
elif choice==3:
    computer_name='诸葛亮'
else:
    computer_name='匿名'
print(player_name,'VS',computer_name)
while True:
    #玩家出拳
    player_fist=eval(input('-----------请出拳：1.石头   2.剪刀   3.布-----------------\n'))
    if player_fist==1:
        player_fist_name='石头'
    elif player_fist==2:
        player_fist_name='剪刀'
    elif player_fist == 3:
        player_fist_name = '布'
    else:
        player_fist_name='石头' #默认出石头
        player_fist=1

    #电脑角色出拳
    computer_fist=random.randint(1,3)
    if computer_fist==1:
        computer_fist_name='石头'
    elif computer_fist==2:
        computer_fist_name='剪刀'
    elif computer_fist == 3:
        computer_fist_name = '布'
    else:
        computer_fist_name='布' #默认出布
    print(player_name,'出拳：',player_fist_name)
    print(computer_name,'出拳：',computer_fist_name)
    if player_fist==computer_fist:
        print('平局！')
    elif (player_fist==1 and computer_fist==2) or (player_fist==2 and computer_fist==3) or (player_fist==3 and computer_fist==1):
        print('玩家',player_name,'胜！')
        player_score+=1
    else:
        print('电脑',computer_name,'胜！')
        computer_score+=1
    answer=input('是否再来一局？y/n')
    if answer!='y':
        break
print('-----------------------------------')
print(player_name,player_score)
print(computer_name,computer_score)
print('-----------------------------------')
if player_score==computer_score:
    print('平局')
elif player_score>computer_score:
    print(player_name,'胜利')
else:
    print(computer_name,'胜利')
