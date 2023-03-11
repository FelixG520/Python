year=int(input("请输入年份:"))
month=int(input("请输入月份:"))
day1=[1,3,5,7,8,10,12]
day2=[4,6,9,11]
#四年一闰；百年不闰，四百年再闰
if(year%4==0 and year%100!=0 & year%400==0):       #and也可用&替代
    print(year, "是闰年")
    if (month == 2):
        print(year, "年", month, "月有", 29, "天")
else:
    print(year, "是平年")
    if (month == 2):
        print(year, "年", month, "月有", 28, "天")

if(month in day1):
    print(year,"年",month,"月有",31,"天")
elif(month in day2):
    print(year,"年",month,"月有",30,"天")
else:
    print("月份输入错误！")