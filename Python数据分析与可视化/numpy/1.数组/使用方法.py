import numpy as np

print(np.ones((2,3)))  #创建一个全0的数组

print(np.zeros((3,4)))  #创建一个全1的数组

print(np.eye(3))  #对角线为1的正方形数组

t=np.arange(24).reshape(4,6)
print(t)

print(np.argmax(t,axis=0)) #每一列最大位置的索引
print(np.argmin(t,axis=0)) #每一列最小位置的索引