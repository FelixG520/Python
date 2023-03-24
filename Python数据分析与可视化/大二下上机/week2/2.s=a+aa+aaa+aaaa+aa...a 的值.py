#求 s=a+aa+aaa+aaaa+aa...a 的值，其中 a 是一个数字。例如 2+22+222+2222+22222(此时共有 5 个数相加)，几个数相加由键盘控制。

i=int(input("你想几个数字相加："))
a=int(input("请输入一个数字："))
s=0
n=0
m=i
while n < i :
    s += m * a * 10**n
    n += 1
    m -= 1
print(s)