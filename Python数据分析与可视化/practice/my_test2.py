from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

#设置字体
my_font = font_manager.FontProperties(fname="C:WINDOWS\FONTS\MSYH.TTC")

#x和y轴
x= [i for i in range(11,31)]
y1= [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2= [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]

#图大小
plt.figure(figsize=(20,8),dpi=80)


#绘制
plt.plot(x,y1,label="自己",color="orange",linestyle=':',linewidth=5)
plt.plot(x,y2,label="同桌",color="cyan",linestyle='-.',linewidth=5)

#刻度
_xtick_labels=["{}岁".format(i) for i in range(11,31)]

#数字和字符串一一对应，数据的长度一样
plt.xticks(list(x),_xtick_labels,fontproperties=my_font)

#设置y轴长度
plt.yticks(range(0,9))

#添加描述信息 -- 显示中文要添加fontproperties参数
plt.xlabel("年龄",fontproperties=my_font)
plt.ylabel("个数",fontproperties=my_font)
plt.title("11岁到30岁男（女）朋友的数量",fontproperties=my_font)

#绘制网格
plt.grid(linestyle='--')

#添加图例
#prop=my_font -- 设置字体
#loc="upper left" -- 图例左上角
plt.legend(prop=my_font,loc="upper left")

#展示
plt.show()