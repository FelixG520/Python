import numpy as np

#****************** 一维数组 **********************
print("*"*40,"一维数组","*"*40)
arr = np.arange(10)
print("*"*20,"print(arr)","*"*20)
print(arr)
print("*"*20,"print(arr[5])","*"*20)
print(arr[5]) #索引为5的元素
print("*"*20,"print(arr[5:8])","*"*20)
print(arr[5:8]) #索引为5 - 8的元素

#改变索引为5 - 8的元素的值
arr[5:8]=12
print("*"*20,"print(arr)","*"*20)
print(arr)

#视图上的任何修改都会直接反映到源数组上
arr_slice=arr[5:8]
print("*"*20,"print(arr_slice))","*"*20)
print(arr_slice)

arr_slice[1]=12345
print("*"*20,"print(arr)","*"*20)
print(arr)

#切片[ : ]会给数组中的所有值赋值
arr_slice[:]=64
print("*"*20,"print(arr)","*"*20)
print(arr)

#**************** 多维数组 *****************
print("*"*40,"二维数组","*"*40)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("*"*20,"print(arr2d[2]))","*"*20)
print(arr2d[2]) #索引2是个数组
print("*"*20,"print(arr2d[0][2])","*"*20)
print(arr2d[0][2]) #(1,3)元素
print("*"*20,"print(arr2d))","*"*20)
print(arr2d)
print("*"*20,"print(arr2d[:2])","*"*20)
print(arr2d[:2]) #索引0，1的数组
print("*"*20,"print( arr2d[:2, 1:])","*"*20)
print( arr2d[:2, 1:]) #切行和列
print("*"*20,"print( arr2d[1, :2])","*"*20)
print( arr2d[1, :2])#第二行的前两列
print("*"*20,"print(arr2d[:2, 2])","*"*20)
print(arr2d[:2, 2])#第三列的前两行
print("*"*20,"print(arr2d[:, :1])","*"*20)
print(arr2d[:, :1]) #每个数组的第一个元素
arr2d[:2, 1:] = 0
print("*"*20,"print(arr2d)","*"*20)
print(arr2d)

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("*"*20,"print(arr3d)","*"*20)
print(arr3d)
print("*"*20,"print(arr3d[0])","*"*20)
print(arr3d[0]) #索引0是一个二维数组


old_values = arr3d[0].copy()
arr3d[0] = 42
print("*"*20,"print(old_values)","*"*20)
print(old_values) #保存原数组
print("*"*20,"print(arr3d[0])","*"*20)
print(arr3d[0]) #修改索引0的二维数组的值
arr3d[0]=old_values
print("*"*20,"print(arr3d)","*"*20)
print(arr3d) #把源数据还原

#************************　布尔型索引　***************************
print("*"*40,"布尔型索引","*"*40)
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print("*"*20,"print(names)","*"*20)
print(names)
print("*"*20,"print(names=='Bob')","*"*20)
print(names=='Bob') #比较运算将会产生一个布尔型数组

data = np.random.randn(7, 4)
print("*"*20,"data = np.random.randn(7, 4)","*"*20)
print(data)

print("*"*20,"print(data[names == 'Bob'])","*"*20)
print(data[names == 'Bob'])#布尔型数组可用于数组索引 -- 布尔型数组的长度必须跟被索引的轴长度一致
print("*"*20,"print(data[names == 'Bob', 2:])","*"*20)
print(data[names == 'Bob', 2:])

#要选择除"Bob"以外的其他值，既可以使用不等于符号（!=），也可以通过~对条件进行否定
print("*"*20,"print(names != 'Bob')","*"*20)
print(names != 'Bob')

print("*"*20,"print(data[~(names == 'Bob')])","*"*20)
print(data[~(names == 'Bob')])

#~操作符用来反转条件
cond = names == 'Bob'
print("*"*20,"cond = names == 'Bob'","*"*20)
print(data[~cond])
#选取这三个名字中的两个需要组合应用多个布尔条件
mask = (names == 'Bob') | (names == 'Will')
print("*"*20,"print(mask)","*"*20)
print(mask)
print("*"*20,"print(data[mask])","*"*20)
print(data[mask])


#将data中的所有负值都设置为0
data[data < 0] = 0
print("*"*20,"data[data < 0] = 0","*"*20)
print(data)
data[names != 'Joe'] = 7
print("*"*20,"data[names != 'Joe'] = 7","*"*20)
print(data)


#******************** 花式索引 ***********************
print("*"*40,"花式索引","*"*40)
arr = np.empty((8, 4))
print("*"*20,"arr = np.empty((8, 4))","*"*20)
for i in range(8):
    arr[i] = i
print(arr)

print("*"*20,"print(arr[[4, 3, 0, 6]])","*"*20)
print(arr[[4, 3, 0, 6]])

print("*"*20,"print(arr[[-3, -5, -7]])","*"*20)
print(arr[[-3, -5, -7]])

arr = np.arange(32).reshape((8, 4))
print("*"*20,"arr = np.arange(32).reshape((8, 4))","*"*20)
print(arr)

print("*"*20,"print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])","*"*20)
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])

print("*"*20,"print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])","*"*20)
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
