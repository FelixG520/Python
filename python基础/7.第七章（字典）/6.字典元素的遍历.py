# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
·字典元素的遍历
      for item in scores:
           print(item)
'''


scores= {'张三':100,'李四':98,'王五':45}
#字典元素的遍历
for item in scores:
    print(item)
    print(item,scores[item],scores.get(item))


