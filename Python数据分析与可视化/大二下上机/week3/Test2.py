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
print(result)
