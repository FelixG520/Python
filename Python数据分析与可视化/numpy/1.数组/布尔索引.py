import numpy as np

t=np.arange(24).reshape((4,6))
print(t<10) #数组中小于10的数

t[t>20]=20 #大于20的数改为20
print(t)

#把t中小于10的数字替换为0，把大于10的替换为10
print(np.where(t<10,0,10))

#小于10的替换为10，大于18的替换为了18
print(t.clip(10,18))

#把(3,3)值换成nan
t=t.astype(float)
t[3,3]=np.nan
print(t)