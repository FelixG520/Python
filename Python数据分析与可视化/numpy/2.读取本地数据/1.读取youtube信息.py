import numpy as np
us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
t2 = np.loadtxt(us_file_path,delimiter=",",dtype="int")
print(t1)
print("*"*100)
print(t2)


print("*"*100)

#取行
print(t2[2]) #第三行

print("*"*100)
#连续多行
print(t2[2:]) #从第三行开始
#不连续多行
print("*"*100)

print(t2[[3,5,7]]) #取4，6，8行

#取列 -- 逗号前表示行，逗号后表示列，冒号表示所有
print("*"*100)

print(t2[1,:]) #第二行所有列
print("*"*100)

print(t2[2:,:]) #第三行开始所有列
print("*"*100)

print(t2[[2,4,6],:])

print("*"*100)
print(t2[:,0]) #第一列

print("*"*100)
print(t2[:,2:]) #连续多列

print("*"*100)
print(t2[:,[1,3]]) #不连续多列

print("*"*100)
print(t2[2,3]) #某一行某一列

print("*"*100)
print(t2[2:5,0:2]) #多行多列 3-5行，1-2列

print("*"*100)
print(t2[[0,2],[0,1]]) #1,3行 1,2列

