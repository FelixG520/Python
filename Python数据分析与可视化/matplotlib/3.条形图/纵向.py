from matplotlib import pyplot as plt
from matplotlib import font_manager
#设置字体
my_font = font_manager.FontProperties(fname="C:WINDOWS\FONTS\MSYH.TTC")
#确定x和y轴
a = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：\n最后的骑士",
     "摔跤吧！爸爸","加勒比海盗5：\n死无对证","金刚：\n骷髅岛","极限特工：\n终极回归",
     "生化危机6：\n终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺",
     "金刚狼3：\n殊死一战","蜘蛛侠：\n英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]
b=[56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]

x=range(len(a))
#设置图大小
plt.figure(figsize=(20,8),dpi=80)

#绘图，并设置尺寸
plt.bar(x,b,width=0.3)

#设置字符串到x轴
plt.xticks(x,a,rotation=25,fontproperties=my_font)


#添加描述信息
plt.xlabel("电影名称",fontproperties=my_font)
plt.ylabel("票房/(亿)",fontproperties=my_font)
plt.title("2017年内地电影票房前20的电影票房数据",fontproperties=my_font)

#保存图片

plt.savefig("./movie.png")
#展示
plt.show()

