# 需求1：制作⼀个计算器，计算任意两数字之和，并保存结果。
print("需求1：制作⼀个计算器，计算任意两数字之和，并保存结果。")
def Add(num1,num2):
    return num1+num2
num1=eval(input("请输入第一个数："))
num2=eval(input("请输入第二个数："))
add=Add(num1,num2)
fp=open('add.txt','a+')
print(num1,"+",num2,"=",add,file=fp)
fp.close()
print(num1,"+",num2,"=",add)
print("\n")

# 需求2：制作⼀个计算器，根据操作符，计算任意两数字之和（差、商、积），并保存结果。
print("需求2：制作⼀个计算器，根据操作符，计算任意两数字之和（差、商、积），并保存结果。")
# 定义函数，根据操作符计算结果
def cal(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("Invalid operator")
        return None
    return result

# 输入数字和操作符
num1 = float(input("请输入第一个数字: "))
num2 = float(input("请输入第二个数字: "))
operator = input("请输入操作符（+、-、*、/）: ")

# 调用函数，计算结果
result = cal(num1, num2, operator)
# 输出结果
fp=open('cal.txt','a+')
print(num1,operator,num2,"=", result,file=fp)
fp.close()
print(num1,operator,num2,"=", result)
print("\n")

# 需求3：打印⼀条横线
print("需求3：打印⼀条横线")

def printLine():
    print("-" * 50)


printLine()

print("\n")

# 需求4：打印多条横线
print("需求4：打印多条横线")
num = int(input("请输入要打印的行数："))


def printNum(num):
    i = 0
    while i < num:
        printLine()
        i += 1


printNum(num)
print("\n")

# 需求5：任意三个数之和
import random

print("需求5：任意三个数之和")
num1 = random.randint(1, 10000)
num2 = random.randint(1, 10000)
num3 = random.randint(1, 10000)


def Sum(a, b, c):
    return a + b + c


sum = Sum(num1, num2, num3)
print(num1, "+", num2, "+", num3, "=", sum)
print("\n")

# 需求6：任意三个数求平均值
print("需求6：任意三个数求平均值")


def Avr():
    avr = Sum(num1, num2, num3) / 3
    return avr


avr = Avr()
print("(", num1, "+", num2, "+", num3, ")/3", "=", avr)
print("\n")

# 需求7：元组数据拆包：
print("需求7：元组数据拆包：")
person = ('Alice', 25, 'female')
name, age, gender = person
print(name,age,gender)
print("\n")

# 需求8：字典数据拆包：
print("需求8：字典数据拆包：")
person = {'name': 'Alice', 'age': 25, 'gender': 'female'}
name, age, gender = person.values()
print(name,age,gender)
print("\n")

# 需求9：Python函数递归调用，比如100以内的数相加f(100)=100+f(99)+....
print("需求9：Python函数递归调用，比如100以内的数相加f(100)=100+f(99)+....")

# result = 1+2+3+.....99+100

Num = int(input("请输入前num项和的num:"))
def sum_num(num):
    # num =2
    if num == 1:
        return 1
    # 返回值 自己调用自己
    return num + sum_num(num - 1)

sum_Num = sum_num(Num)
print("1+2+3+...+",Num,"=", sum_Num)

# 斐波那契数列
print("斐波那契数列")

def fib(n):
    """递归函数实现斐波那契数列"""
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

while(True):
    n = int(input("请输入数列的项数："))
    if n >= 35:
        print("太大了，递归深度过大，电脑负荷太大！")
        continue;
    else:
        for i in range(1,n):
            res = fib(i)
            print(res,end=" ")
        break;
