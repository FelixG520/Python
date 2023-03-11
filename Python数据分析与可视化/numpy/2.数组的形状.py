import numpy as np
t1=np.arange(12)
print(t1)    #[ 0  1  2  3  4  5  6  7  8  9 10 11]
print(t1.shape)  #(12,) -- 一维数组元素个数

t2=np.array([[1,2,3],[4,5,6]])
print(t2)  #[[1 2 3][4 5 6]]
print(t2.shape)  #(2, 3) -- 二维数组行列

t3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(t3)
'''[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]'''
print(t3.shape)  #(2, 2, 3) -- 三维矩阵 -- 块数行列


#修改数组形状
t4=np.arange(12).reshape(3,4) #转二维数组
print(t4)
print(t4.shape) #(3, 4)

t5=np.arange(24).reshape(2,3,4) #转三维数组
print(t5)
print(t5.shape) #(2, 3, 4)

t5=np.arange(24).reshape(4,6) #转二维数组
print(t5)
print(t5.shape) #(4, 6)

t5=np.arange(24).reshape(24,1) #转二维数组
print(t5)
print(t5.shape) #(24, 1)

t6=t5.reshape((t5.shape[0]*t5.shape[1],))  #转一维数组
print(t6)  #转成一维数组

#将多维数组直接转成一维数组
t7=t5.flatten()
print(t7)