import numpy as np

#1.两个nan是不相等的
print(np.nan==np.nan)
print(np.nan!=np.nan)

#2.判断数组中非零的个数
t=np.arange(24).reshape(4,6)
print(t)
t[:,0] = 0
print(t)
print(np.count_nonzero(t)) #20

#3.如何判断一个数字是否为nan呢?
t=t.astype(float)
t[3,3]=np.nan
print(t)
print(t!=t)

print(np.count_nonzero(t!=t)) #1

print(np.isnan(t))

#4.nan和任何值计算都是nan
print(np.sum(t)) #nan

t2=np.arange(12).reshape(3,4)
print(t2)
print(np.sum(t2))
print(np.sum(t2,axis=0))
print(np.sum(t2,axis=1))
print(np.sum(t,axis=0))
print(np.sum(t,axis=1))