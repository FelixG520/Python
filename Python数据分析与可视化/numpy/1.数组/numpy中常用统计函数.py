import numpy as np

t=np.arange(12).reshape(3,4)
print(t)

#求和
print(np.sum(t)) #66
print(np.sum(t,axis=0)) #[12 15 18 21]
print(np.sum(t,axis=1)) #[ 6 22 38]

#均值
print(np.mean(t)) #5.5
print(np.mean(t,axis=0)) #[4. 5. 6. 7.]
print(np.mean(t,axis=1)) #[1.5 5.5 9.5]

#中值
print(np.median(t)) #5.5
print(np.median(t,axis=0)) #[4. 5. 6. 7.]
print(np.median(t,axis=1)) #[1.5 5.5 9.5]

#最大值
print(np.max(t)) #11
print(np.max(t,axis=0)) #[ 8  9 10 11]
print(np.max(t,axis=1)) #[ 3  7 11]

#最小值
print(np.min(t)) #0
print(np.min(t,axis=0)) #[0 1 2 3]
print(np.min(t,axis=1)) #[0 4 8]

#极值
print(np.ptp(t)) #11
print(np.ptp(t,axis=0)) #[8 8 8 8]
print(np.ptp(t,axis=1)) #[3 3 3]

#标准差
print(np.std(t)) #3.452052529534663
print(np.std(t,axis=0)) #[3.26598632 3.26598632 3.26598632 3.26598632]
print(np.std(t,axis=1)) #[1.11803399 1.11803399 1.11803399]