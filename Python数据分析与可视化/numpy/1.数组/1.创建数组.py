import random
import numpy as np
t1=np.array([1,2,3])
print(t1)
print(type(t1))

t2=np.array(range(10))
print(t2)
print(type(t2))

t3=np.arange(12)
print(t3)
print(t3.dtype)

t4=np.arange(4,10,2)
print(t4)

#numpy中的数据类型
t5=np.array(range(1,4),dtype="float32")
print(t4)
print(t4.dtype)
#布尔类型
t6=np.array([1,1,0,1,0,0],dtype=bool)
print(t6)
print(t6.dtype)

#调整数据类型
t7=t6.astype("int32")
print(t6)
print(t6.dtype)

#numpy中的小数
t8=np.array([random.random() for i in range(10)])
print(t8)
print(t8.dtype)

t9=np.round(t8,2)#保留两位小数
print(t9)
print(t9.dtype)