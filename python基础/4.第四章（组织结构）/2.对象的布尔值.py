# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

#Python一切皆对象，所有对象都有一个布尔值
  #·获取对象的布尔值：使用内置函数bool（）

'''以下对象的布尔值为False
   ·False
   ·数值（）
   ·0
   ·None
   ·空字符串
   ·空列表
   ·空元组
   ·空字典
   ·空集合
   '''
print('---------------以下对象的布尔值为False----------------------')
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(''''''))
print(bool([]))        #空列表
print(bool(list()))    #空列表
print(bool(()))        #空元组
print(bool(tuple()))   #空元组
print(bool({}))        #空子典
print(bool(dict()))    #空子典
print(bool(set()))     #空集合
print('---------------其他对象的布尔值均为Ture----------------------')
print(bool(18))
print(bool(True))
print(bool('helloworld'))


age=int(input('请输入你的年龄：'))
if age:                        #整数的布尔值为Ture，所以print(age)
    print(age)
else:
    print('年龄为:',age)        #0的布尔值为Fslae，所以print('年龄为:',age)
