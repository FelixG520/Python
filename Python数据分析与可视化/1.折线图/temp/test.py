from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

#设置字体
my_font = font_manager.FontProperties(fname="C:WINDOWS\FONTS\MSYH.TTC")

#x和y轴
x=range(0,120)
y= [ random.randint(20,35) for i in range(120)]

#图大小
plt.figure(figsize=(20,8),dpi=80)


#绘制
plt.plot(x,y)

#刻度
_xtick_labels=["10点:{}分".format(i) for i in range(60)]  #表示0-60分钟
_xtick_labels += ["11点:{}分".format(i) for i in range(60)] #表示60-120分钟

#取步长，数字（list(x)[::3]）和字符串（_xtick_labels[::3]）一一对应，数据的长度一样
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=30,fontproperties=my_font)#rotation=30 -- 横坐标旋转30度

#添加描述信息 -- 显示中文要添加fontproperties参数
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度 单位(℃)",fontproperties=my_font)
plt.title("10点到12点每分钟的气温变化情况",fontproperties=my_font)

#展示
plt.show()