# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

'''key的判断'''
scores= {'张三':100,'李四':98,'王五':45}
print('张三' in scores)
print('张三' not in scores)


del scores['张三']  #删除指定的key-valu对
print(scores)
#del scores   直接把字典删除
scores.clear()     #清空字典的元素
print(scores)

#字典元素的新增操作
scores['陈六']=98     #新增元素
print(scores)

scores['陈六']=100    #修改元素
print(scores)


