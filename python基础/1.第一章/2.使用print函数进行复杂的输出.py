'''
·print()函数的完整语法格式
def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
    self:对象
    *args:可以输出多个对象
    sep=' ':输出用空格隔开
    end='\n':输出完一句换行
'''

print('北京',end='--->')
print('欢迎你')

print(1314)
print(3.14)
print(1,3,1,4)   #使用逗号连接要输出的数字，中间使用空格还接
print(192,168,1,1,sep='.') #使用间隔符进行连接,数值之间用.分隔
#print('北京欢迎你'+2022)   报错
print('北京欢迎你'+"2022")

fp=open('text','w')
print('人生苦短，我用python',file=fp)
fp.close()