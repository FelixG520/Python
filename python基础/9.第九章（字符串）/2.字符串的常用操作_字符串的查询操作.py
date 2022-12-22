# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


'''把字符串看成关于字符的列表

·字符串的查询操作
  ·查询方法
      ·index()   查找子串substr第一次出现的位置，如果查找的子串不存在时，则抛出ValueError
      ·rindex()  查找子串substr最后一次出现的位置，如果查找的子串不存在时，则抛出ValueError
      ·find()    查找子串substr第一次出现的位置，如果查找的子串不存在时，则返回-1.什么叫模块_模块化编程的好处
      ·rfind()   查找子串substr最后一次出现的位置，如果查找的子串不存在时，则返回-1.什么叫模块_模块化编程的好处
      '''

s='hello,hello'
print(s.index('lo'))       #3
print(s.find('lo'))        #3
print(s.rindex('lo'))      #9
print(s.rfind('lo'))       #9


#print(s.index('k'))      ValueError: substring not found
print(s.find('k'))
print(s.rfind('k'))