import numpy as np

t=np.arange(24).reshape((4,6))
print(t)
print(t.transpose())
print(t.T)
print(t.swapaxes(1,0)) #1和0轴交换

