'''
企业发放的奖金根据利润提成。利润(I)低于或等于 10 万元时，奖金可提 10%；
利润高于 10 万元，低于 20 万元时，低于 10 万元的部分按 10%提成，高于 10 万元的部分，可可提成 7.5%；
20 万到 40 万之间时，高于 20 万元的部分，可提成 5%；
40 万到 60 万之间时高于 40 万元的部分， 可提成 3%；
60 万到 100 万之间时， 高于 60 万元的部分， 可提成 1.5%，
高于 100 万元时，超过 100 万元的部分按 1%提成，
从键盘输入当月利润，求应发放奖金总数？
'''

money = int(input('请输入月利润：'))
standard1=100000
standard2=200000
standard4=400000
standard6=600000
standard10=1000000

if money < 0:
    bonus = 0
elif (money <= standard1):
    bonus = money * 0.1

elif (money >= standard1) and (money <= standard2):
    bonus = (money - standard1) * 0.075 + standard1 * 0.1

elif (money >= standard2) and (money <= standard4):
    bonus = standard1 * 0.175 + (money - standard2) * 0.05

elif (money >= standard4) and (money <= standard6):
    bonus = standard1 * 0.175 + standard2 * 0.03 + (money - standard4) * 0.05

elif (money >= standard6) and (money <= standard10):
    bonus = standard1 * 0.175 + standard2 * 0.08 + (money - standard6) * 0.015

else:
    bonus = standard1 * 0.175 + standard2 * 0.08 + standard4 * 0.015 + (money - standard1) * 0.01
print('当月奖金为', bonus)