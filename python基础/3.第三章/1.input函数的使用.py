# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


#输入函数input
present=input('张三想要什么礼物呢？')
print(present,type(present))

#练习题：从键盘录入两个整数，计算两个整数的和
a=input('请输入一个加数：')   #10
b=input('请输入另一个加数：')   #20
print(type(a),type(b))       #均为str类型
print(a+b)                   #输出1020，说明+起到连接作用，应进行数据类型转换，应转成int类型

print('---------------第一种转换方式---------------')
a=input('请输入一个加数：')
a=int(a)                       #将转换之后的结果存储到a中
b=input('请输入另一个加数：')
b=int(b)
print(type(a),type(b))       #都为int类型
print(a+b)                   #10+20=30
print('---------------第二种转换方式---------------')
a=int(input('请输入一个加数：'))
b=int(input('请输入另一个加数：'))
print(type(a),type(b))
print(a+b)


