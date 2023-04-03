num1=eval(input("请输入第一个数字："))
num2=eval(input("请输入第二个数字："))
num3=eval(input("请输入第三个数字："))

print("三个数的和是：",num1+num2+num3)
print("三个数的平均数是：",(num1+num2+num3)/3)

print("三个数的平均数是：%.2f" , (num1+num2+num3)/3)    #双引号内的内容直接输出
print("三个数的平均数是：%.2f" % ((num1+num2+num3)/3))  #格式化字符串，%作占位符
print("三个数的平均数是：{0:.2f}" .format((num1+num2+num3)/3))  #格式化字符串，{}作占位符
print(f"三个数的平均数是：{(num1+num2+num3)/3}" )  #格式化字符串，f-string方法