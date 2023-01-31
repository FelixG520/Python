# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

'''常用的运算符
     1.算术运算符
          ·标准算术运算符
          ·取余运算符
          ·幂运算符
     2.赋值运算符
     3.比较运算符
     4.布尔运算符
     5.位运算符'''
                                    #1.算数运算符
print('1.算数运算符')
print('------------标准运算符-------------')
print('1+1 =',1+1)   #加法运算
print('1-1 = ',1-1)   #减法运算
print('2*4=',2*4)   #乘法运算
print('1/2=',1/2)   #除法运算
print('11/2',11/2)  #除法运算
print('11//2=',11//2) #整除运算
print('------------带负号的情况-------------')
print('9//4=',9//4)     #2
print('-9//-4=',-9//-4)   #2
print('-9//4=',-9//4)    #-3   一正一负的整除公式：向下取整（高斯取整函数）
print('9//-4=',9//-4)    #-3
print('9%-4=',9%-4)     #-3   一正一负的取余公式：余数=被除数-除数*商    9-（-4）*（-3）=9-12=-3
print('-9%4=',-9%4)     #3                                          -9-4*（-3）=-9+12=3
print('------------取余运算符-------------')
print('11%2=',11%2)  #取余运算
print('------------幂运算符-------------')
print('2**2=',2**2)  #幂运算（表示2的2次方）
print('2**3=',2**3)  #幂运算（表示2的3次方）   2*2*2=8



                            #2.赋值运算符，运算顺序从左到右
print('2.赋值运算符，运算顺序从左到右')
i=3+4     #从左到右a<--7
print(i)
print('---------------支持链式赋值--------------')
a=b=c=20     #链式赋值
print(a,id(a))
print(b,id(b))
print(c,id(c))
print('---------------支持参数赋值--------------')
a=20
a+=30     #相当于a=a+30
print(a)
a-=10     #相当于a=a-10
print(a)
a*=2      #相当于a=a*2
print(a,type(a))
a/=3      #相当于a=a/3
print(a,type(a))
a//=2     #相当于a=a//3
print(a,type(a))
a%=3      #相当于a=a%3
print(a,type(a))
print('---------------支持系列解包赋值--------------')
a,b,c=20,30,40
print(a,b,c)
#a,b=20,30,40    报错，因为左右变量的个数和值的个数不对应
print('---------------交换两个变量的值--------------')
a,b=20,30
print('交换之前：',a,b)
a,b=b,a
print('交换之后：',a,b)



                                       #3.比较运算符
print('3.比较运算符')
'''对变量或表达式的结果进行大小、真假的比较（结果是bool类型）
   ·>、<、>=、<=、!=
   ·==-->对象value的比较
   ·is、is not-->对象id的比较'''
print('---------------比较运算符--------------')
a,b=20,30
print('a>b吗?',a>b)   #False
print('a<b吗?',a<b)   #Ture
print('a>=b吗?',a>=b)
print('a<=b吗?',a<=b)
print('a==b吗?',a==b)
print('a!=b吗?',a!=b)
'''"="称为赋值运算符,"=="称为比较运算符
    一个变量由三部分组成:标识、类型、值
    ==比较的是值还是表示呢?比较的是值
    比较对象的标识使用  is
    '''
a=10
b=10
print(a==b)    #Ture   说明a与b的value相等
print(a is b)  #Ture   说明a与b的id标识相等
#以下代码没学过,以后进行学习
list1=[11,22,33,44]
list2=[11,22,33,44]
print(list1==list2)   #value-->Ture
print(list1 is list2) #id-->False
print(id(list1))
print(id(list2))
print(a is not b)  #False   a的id与b的id是不相等的
print(list1 is not list2) #True   list1的id与list2的id是不相等的



                           #4.布尔运算符
print('4.布尔运算符')
#布尔运算符:and、or、not、in、not in
print('---------------布尔运算符--------------')
a,b=1,2
print('and表示并且')
print(a==1 and b==2)   #Ture+Ture=Ture
print(a==1 and b<2)    #Ture+False=False
print(a!=1 and b==2)   #False+Ture=False
print(a!=1 and b!=2)   #False+False=False
print('or表示或者')
print(a==1 or b==2)    #Ture or Ture=Ture
print(a==1 or b<2)    #Ture or False=Ture
print(a!=1 or b==2)   #False or Ture=Ture
print(a!=1 or b!=2)   #False or False=False
print('not表示非,对bool类型的操作数取反')
f1=True
f2=False
print(not f1)
print(not f2)
print('in表示在……里，not in表示不在……里')
s='helloworld'
print('w' in s)       #Ture，w在helloworld中
print('k' in s)       #False，k不在helloworld中
print('w' not in s)   #False，w在helloworld中
print('k' not in s)   #Ture，k不在helloworld中


                                     #5.位运算符
#将数据转成二进制进行计算
'''位运算符
   ·位与&-->对应数位都是1，结果数位才是1，否则为0
   ·位与|-->对应数位都是0，结果数位才是0，否则为1
   ·左位移运算符<<   -->高位溢出舍弃，低位补0
   ·右位移运算符>>   -->低位溢出舍弃，高位补0'''
print('5.位运算符')
print('\'&按位与\',\'|按位或\'')
print(4&8)    #都是1，结果数位才是1
print(4|8)    #都是0，结果数位才是0
print(4<<1)   #向左移动一位，相当于乘以2
print(4<<2)   #向左移动两位，相当于乘以4
print(4>>1)   #向右移动一位，相当于除以2
print(4>>2)   #向右移动两位，相当于除以4


                                     #6.内置函数
#divmod()函数把除数和余数运算结果结合起来,返回一个包含商和余数的元组(a//b, a%b)
print('6.内置函数')
print('divmod()函数把除数和余数运算结果结合起来,返回一个包含商和余数的元组(a//b, a%b)')
g=10
h=4
print(divmod(g,h))


print('pow()函数是内置函数。它接收两个参数,x和y,pow(x,y)函数返回的是x的y次方的值。')
print(pow(g,h))