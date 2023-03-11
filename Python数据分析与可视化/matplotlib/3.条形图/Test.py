from matplotlib import pyplot as plt
from matplotlib import font_manager
#设置字体
my_font = font_manager.FontProperties(fname="C:WINDOWS\FONTS\MSYH.TTC")
#确定x和y轴
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

bar_width=0.2
x_14=list(range(len(a)))
x_15=[i+bar_width for i in x_14]#往右移一个width的距离，否则可能重叠
x_16=[i+bar_width*2 for i in x_14]
#设置图大小
plt.figure(figsize=(20,8),dpi=80)

#绘图，并设置尺寸
plt.bar(x_16,b_16,width=bar_width,color="orange",label="9月14日")
plt.bar(x_15,b_15,width=bar_width,color="red",label="9月15日")
plt.bar(x_14,b_14,width=bar_width,color="blue",label="9月16日")

#设置图例
plt.legend(prop=my_font)

#绘制网格
plt.grid(alpha=0.3)

#设置字符串到x轴
plt.xticks(x_15,a,fontproperties=my_font)


#添加描述信息
plt.xlabel("电影名称",fontproperties=my_font)
plt.ylabel("票房/(亿)",fontproperties=my_font)
plt.title("2017年内地电影票房前20的电影票房数据",fontproperties=my_font)



#保存图片
plt.savefig("./movie.png")
#展示
plt.show()

