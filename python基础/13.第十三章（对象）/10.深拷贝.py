# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
·深拷贝
  ·使用copy模块的deepcopy函数,递归拷贝对象中包含的子对象,源对像和拷贝对象所有的子对象也不相同
'''
#深拷贝
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
#变量的赋值
cpu1=CPU()       #<__main__.CPU object at 0x000001820F818550>   一个对象对应两个变量
cpu2=cpu1        #<__main__.CPU object at 0x000001820F818550>
print(cpu1)
print(cpu2)

print('-------------------------------------------')
disk=Disk()   #创建一个硬盘类的对象
computer=Computer(cpu1,disk)    #创建一个计算机类的对象


#深拷贝
import copy
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)

#深拷贝 直接把另一个对象的子对象和另一个对象都拷贝并且内存地址都变了