import numpy as np

print(np.random.randint(10,20,(4,5))) #4行5列数组，元素范围在10-20

np.random.seed(10)
t = np.random.randint(0,20,(3,4))
print(t)