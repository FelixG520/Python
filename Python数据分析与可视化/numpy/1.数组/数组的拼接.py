import numpy as np

t1=np.arange(12).reshape(2,6)
print(t1)
t2=np.arange(12,24).reshape(2,6)
print(t2)

print(np.vstack((t1,t2)))  #竖直拼接
print(np.hstack((t1,t2)))  #水平拼接