'''
实战一
-题目:“千年虫”是什么虫
需求:已知一个列表中存储的是员工的出生年份
[88,89,90,98,00,99]，由于时间比较久，出生的年份均为2位整数，
现需要2位年份前加19，如果年份是00，将需要加上200

'''

lst=[88,89,90,98,00,99]
print('原列表：',lst)
#遍历列表
for index in range(len(lst)):
    if str(lst[index])!='0':
        lst[index]='19'+str([index])
    else:
        lst[index]='200'+str(lst[index])

#修改后的年份列表
print(lst)

#使用enumerate函数遍历列表
for index,value in enumerate(lst):
    if str(value)!='0':
        lst[index]='19'+str(value)
    else:
        lst[index]='200'+str(value)
print(lst)