import numpy as np

t=np.arange(12,24).reshape(3,4)
print(t)

t[[1,2],:]=t[[2,1],:] #行交换
print(t)
t[:,[0,2]]=t[:,[2,0]] #列交换
print(t)