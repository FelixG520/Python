# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

#eval()将字符串类型转换为集合
setA=eval(input('请输入一个集合：'))    #{10,20,30,40}
setB=eval(input('再输入一个集合：'))    #{20,30,40,50,60}
print('交集：',setA&setB)             #交集&
print('并集：',setA|setB)             #并集|
print('setA-setB：',setA-setB)


print(type(setA),type(setB))