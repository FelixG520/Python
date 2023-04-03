import numpy as np

t5=np.arange(24).reshape(4,6) #转二维数组
print(t5)
print(t5.shape) #(4, 6)

print(t5+2)
'''
[[ 2  3  4  5  6  7]
 [ 8  9 10 11 12 13]
 [14 15 16 17 18 19]
 [20 21 22 23 24 25]]
'''
print(t5*2)
'''
[[ 0  2  4  6  8 10]
 [12 14 16 18 20 22]
 [24 26 28 30 32 34]
 [36 38 40 42 44 46]]
'''
print(t5/2)
'''
[[ 0.   0.5  1.   1.5  2.   2.5]
 [ 3.   3.5  4.   4.5  5.   5.5]
 [ 6.   6.5  7.   7.5  8.   8.5]
 [ 9.   9.5 10.  10.5 11.  11.5]]
'''
print(t5/0)
'''
[[nan inf inf inf inf inf]
 [inf inf inf inf inf inf]
 [inf inf inf inf inf inf]
 [inf inf inf inf inf inf]]
'''
t6=np.arange(100,124).reshape((4,6))
print(t6)
print(t6+t5)
'''
[[100 102 104 106 108 110]
 [112 114 116 118 120 122]
 [124 126 128 130 132 134]
 [136 138 140 142 144 146]]
'''
print(t6*t5)
'''
[[   0  101  204  309  416  525]
 [ 636  749  864  981 1100 1221]
 [1344 1469 1596 1725 1856 1989]
 [2124 2261 2400 2541 2684 2829]]
'''
print(t6/t5)
'''
[[         inf 101.          51.          34.33333333  26.
   21.        ]
 [ 17.66666667  15.28571429  13.5         12.11111111  11.
   10.09090909]
 [  9.33333333   8.69230769   8.14285714   7.66666667   7.25
    6.88235294]
 [  6.55555556   6.26315789   6.           5.76190476   5.54545455
    5.34782609]]
'''
t7=np.arange(0,6)
print(t5)
'''
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]
'''
print(t7)
'''
[0 1 2 3 4 5]
'''
print(t5-t7)
'''
[[ 0  0  0  0  0  0]
 [ 6  6  6  6  6  6]
 [12 12 12 12 12 12]
 [18 18 18 18 18 18]]
'''
t8=np.arange(4).reshape((4,1))
print(t5-t8)
'''
[[ 0  1  2  3  4  5]
 [ 5  6  7  8  9 10]
 [10 11 12 13 14 15]
 [15 16 17 18 19 20]]
'''
t9=np.array(10);
print(t9)
print(t5-t9) #报错，行列都不一样，无法计算

