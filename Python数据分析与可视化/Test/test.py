from matplotlib import pyplot as plt
x = range(2,26,2)
y =[15 , 13 , 14.5, 17, 20, 25 , 26 , 26 , 24, 22, 18 , 15]
#设置图片大小
plt.figure(figsize=(20,10),dpi=80)#figsize=(长,宽)

#绘图
plt.plot(x,y)

#设置x轴的刻度
#plt.xticks(x)#显示我们设置的x=range(2,26,2)值
#plt.xticks(range(2,25)) #x轴更密集 -- 默认步长1
# plt.xticks(range(2,25,0.5)) #！！！error，步长不可以为小数

_xtick_labels = [i*0.5 for i in range(4,49)] #列表生成式

#plt.xticks(_xtick_labels)
#plt.xticks(_xtick_labels[::3]) #步长变3，变的更稀疏
plt.xticks(range(25,50)) #显示25-50
plt.yticks(range(min(y),max(y)+1))
#保存
plt.savefig("./test1.png")#./ -- 当前路径下
plt.savefig("./test1.svg")#<font color='red'>svg这种矢量图格式</font>,放大不会有锯齿


#展示图形
plt.show()