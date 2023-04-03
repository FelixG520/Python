import pandas as pd
import string

t=pd.Series([1,2,31,12,3,4])
print(t)
print(type(t))  #<class 'pandas.core.series.Series'>

#类型转换
t.astype(float)
print(t)

t2=pd.Series([1,2,31,12,3,4],index=list("abcdef"))
print(t2)

#通过字典创建
temp_dict={"name":"zhangsan","age":30,"tel":888888}
t3=pd.Series(temp_dict)
print(t3)


#字典推导式创建字典
a={string.ascii_uppercase[i]:i for i in range(10)}
print(pd.Series(a))

at=pd.Series(a,index=list(string.ascii_uppercase[5:15]))
print(at)


#索引
print(t3["age"])
print(t3["tel"])
print(t3[1])
print(t3[2])
print(t3[0])

#切片
print(t3[:2])
print(t3[1:3])
print(t3[[1,2]])
print(t3[["age","tel"]])
