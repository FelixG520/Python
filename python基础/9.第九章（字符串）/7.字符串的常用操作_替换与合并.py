# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


'''
·字符串的其他操作
   ·字符串替换
     ·replace()   第1个参数指定被替换的子串,第2个参数指定替换子串的字符串,该方法返回替換后得到的字符串,替换前的字符串不发生变化,
                  调用该方法时可以通过第3个参数指定最大替换次数
    ·字符串的合并
       ·join()   将列表或元组中的字符串合并成一个字符串

str.replace(old,news):使用news替换字符串s中所有的old字符串，结果是一个新的字符电
str.center(width,fillchar):字符串str在指定的宽度范围内居中，可以使用fillchar进行填充
str.join(iter):在iter中的每个元素的后面都增加一个新的字符串str
str.strip(chars):从字符串中去掉左侧和右侧chars中列出的字符串
str.lstrip(chars):从字符串中去掉左侧chars中列出的字符串
str.rstrip(chars):从字符串中去掉右侧chars中列出的字符串


'''


s='hello,Python'
print(s.replace('Python','Java'))      #用Java替换了Python     hello,Java
s1='hello,Python,Python,Python'
print(s1.replace('Python','Java',2))   #用Java换Python两次     hello,Java,Java,Python

#字符串在指定的宽度范围内居中
print(s.center(20))
print(s.center(20,'*'))

#去除字符串左右的空格
s='     hello world       '
print(s.strip())

#去除字符串左侧的空格
print(s.lstrip())

#去除字符串右侧的空格
print(s.rstrip())

#去除指定的字符
s3='dl-HelloWorld'
print(s3.strip('ld')) #与顺序无关，只要包含dl
print(s3.lstrip('ld')) #与顺序无关
print(s3.rstrip('ld')) #与顺序无关


lst=['hello','Java','Python'] #列表
print('|'.join(lst))
print(' '.join(lst))


t=('hello','Java','Python')  #元组
print(' '.join(t))


print('*'.join('Python'))    #字符串

'''
数据的处理
-字符串的拼接
    ·使用”+”进行拼接字符串
    ·使用str.join()方法进行拼接字符串
    ·直接拼接
    ·使用格式化字符串进行拼接
-字符串去重
-列表元素去重
'''
s1='hello'
s2='world'
#(1)使用+进行连接
print(s1+s2)


#(2)使用join方法
print(''.join(['hello','world']))
print('*'.join(['Hello','Wrold','Python','JAVA','PHP']))
print('你好'.join(['Hello','Wrold','Python','JAVA','PHP']))

#(3)直接拼接
print('hello','world')

#(4)使用格式化字符串
print('%s%s' % (s1,s2))
print(f'{s1}{s2}')
print('{0}{1}'.format(s1,s2))


#去重
a='helloworldhellowefdaldadlgwaniodiedjsf'
#(1)字符串的拼接和not in
new_a=''
for item in a:
    if item not in new_a:#判断a中的每个字符在new_s中是否存在
        new_a+=item
print(new_a)

#(2)使用索引+not in
new_a2=''
for i in range(len(a)):
    if a[i] not in new_a2:
        new_a2+=a[i]
print(new_a2)

#(3)通过集合去重（无序）+列表的排序
new_a3=set(a)  #结果是集合类型
lst=list(new_a3) #转成列表类型
lst.sort(key=a.index) #将原字符串中的索引作为关键字进行排序
print(''.join(lst))