# 为什么要学习pandas

那么问题来了：numpy已经能够帮助我们处理数据，能够结合matplotlib解决我们数据分析的问题，那么pandas学习的目的在什么地方呢？

 numpy能够帮我们处理处理数值型数据，但是这还不够

很多时候，我们的数据除了数值之外，还有==字符串，还有时间序列==等

比如：我们通过爬虫获取到了存储在数据库中的数据

比如：之前youtube的例子中除了数值之外还有国家的信息，视频的分类(tag)信息，标题信息等

所以，numpy能够帮助我们处理数值，但是pandas除了处理数值之外(基于numpy)，还能够帮助我们处理其他类型的数据



## pandas的常用数据类型

1.Series 一维，带标签数组

2.DataFrame 二维，Series容器

### Series创建

#### 不指定索引

```
t=pd.Series([1,2,31,12,3,4])
print(t)
print(type(t))  #<class 'pandas.core.series.Series'>
```

![image-20230331163317744](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230331163317744.png)

#### 指定索引

```
t2=pd.Series([1,2,31,12,3,4],index=list("abcdef"))
print(t2)
```

![image-20230331163552569](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230331163552569.png)

#### 通过字典创建

```
temp_dict={"name":"zhangsan","age":30,"tel":888888}
t3=pd.Series(temp_dict)
print(t3)
```

![image-20230331163814659](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230331163814659.png)

#### 字典推导式创建字典

```python
import string
a={string.ascii_uppercase[i]:i for i in range(10)}
print(pd.Series(a))
```

![image-20230331164453707](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230331164453707.png)

```
print(pd.Series(a,index=list(string.ascii_uppercase[5:15])))
```

![image-20230331164611546](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230331164611546.png)

为什么类型为float呢?

numpy中nan为float，pandas会自动根据数据类更改

series的dtype类型

那么问题来了，如何修改dtype呢

和numpy的方法一样

#### 类型转换

```
t.astype(float)
```

### Series切片和索引

#### 索引

```
print(t3["age"])
print(t3["tel"])
print(t3[1])
print(t3[2])
print(t3[0])
```

![image-20230331165954335](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230331165954335.png)

#### 切片

```
print(t3[:2])
print(t3[1:3])
print(t3[[1,2]])
```

![image-20230331170047731](C:\Users\gaofan\AppData\Roaming\Typora\typora-user-images\image-20230331170047731.png)