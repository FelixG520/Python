# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''2、计算球体的面积和体积
第一步：分析问题：根据公式：球的表面积=4π*R*R,球的体积=(4/3)π*R*R*R求得。
第二步：设计算法：
输入半径R
计算球表面积与体积
输出结果
第三步：编写程序
创建一个新的文档，命名为计算球体的面积和体积'''

#设置常量π
π=3.1415927
#输入半径R的值
R=input('输入半径R的值:')
#计算表面积与体积
S=4*π*float(R)*float(R)
V=(4.0/3)*π*float(R)*float(R)*float(R)
V2=(4/3)*π*float(R)*float(R)*float(R)

#打印结果
print('S=',S)
print('V=',V,'\nV2=',V2)



#v=(4/3)*π*R*R*R行不行，为什么？  TypeError: can't multiply sequence by non-int of type 'float'
#v=(4/3)*π*R*R*R
#print('v=',v)                 TypeError: can't multiply sequence by non-int of type 'float'