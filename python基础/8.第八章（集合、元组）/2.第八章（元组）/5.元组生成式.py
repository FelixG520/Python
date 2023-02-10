'''
元组生成式
- 与列表生成式的语法相同
- 元组生成式的结果是一个生成器对象，需要转换成元组或列表才能查看到元素内容
- 生成器遍历之后，再想重新遍历必须重新创建一个生成器对象，因为遍历后原生成器对象已经不存在了

'''
t=(i for i in range(1,11))
print(t)#<generator object <genexpr> at 0x000001D901FB9510> -- 生成器对象
#生成器对象可以直接for循环遍历
for item in t:
    print(item,end=' ')

#生成器对象转元组
t=(i for i in range(1,11))
t=tuple(t)
print(t)

#__next__()方法 -- 挨个输出
t=(i for i in range(1,11))
print(t.__next__())
print(t.__next__())
print(t.__next__())
t=tuple(t)#剩余元素
print(t)