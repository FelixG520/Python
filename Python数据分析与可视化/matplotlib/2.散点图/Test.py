from matplotlib import pyplot as plt
from matplotlib import font_manager
#设置字体
my_font = font_manager.FontProperties(fname="C:WINDOWS\FONTS\MSYH.TTC")
#确定x和y轴
y_3  = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
#把两个散点图在同一图分开
x_3=range(1,32)#3月和10月都有31天
x_10=range(51,82)#3月和10月都有31天
#设置图大小
plt.figure(figsize=(20,8),dpi=80)
#绘图
plt.scatter(x_3,y_3,label="3月份")
plt.scatter(x_10,y_10,label="10月份")
#添加图例
plt.legend(loc="upper left",prop=my_font)

#调整x轴刻度
_x=list(x_3)+list(x_10)
_xtick_lables=["3月{}日".format(i) for i in x_3]
_xtick_lables+=["3月{}日".format(i-50) for i in x_10]
plt.xticks(_x[::3],_xtick_lables[::3],rotation=30,fontproperties=my_font)#取步长3


#添加描述信息
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度",fontproperties=my_font)
plt.title("标题",fontproperties=my_font)
#展示
plt.show()

