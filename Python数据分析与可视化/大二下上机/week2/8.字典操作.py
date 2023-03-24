#8、请使用Python定义有3个元素的字典。并对字典元素进行遍历、访问等操作。

#创建
score= {'张三':100,'李四':98,'王五':45}
print(score)

#访问
#第一种方式，使用[]
print(score['张三'])
#print(score['陈六'])         KeyError: '陈六'

#第二种方式，使用get()方法
print(score.get('张三'))
print(type(score.get('张三')))
print(score.get('陈六'))       #None
print(score.get('麻七',99))    #99是在查找‘麻七’所对的value不存在时，提供的一个默认值

#字典元素的遍历
for item in score:
    print(item,score[item],score.get(item),end=' ')
print()


for key,value in score.items():
    print(key,value,end=' ')