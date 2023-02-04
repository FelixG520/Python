# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
类的浅拷贝与深拷贝
·变量的赋值操作
  ·只是形成两个变量,实际上还是指向同一个对象
·浅拷贝
  ·Pythan烤贝一段都是浅拷贝,拷贝时,对象包含的子对象内容不烤贝,因此,源对象与拷贝对象会引用同一个子对象
·深拷贝
  ·使用copy模块的deepcopy函数,递归拷贝对象中包含的子对象,源对像和拷贝对象所有的子对象也不相同
'''


class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
#(1).变量的赋值
cpu1=CPU()       #<__main__.CPU object at 0x000001820F818550>   一个对象对应两个变量
cpu2=cpu1        #<__main__.CPU object at 0x000001820F818550>
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))

#(2).类的浅拷贝
print('-------------------------------------------')
disk=Disk()   #创建一个硬盘类的对象
computer=Computer(cpu1,disk)    #创建一个计算机类的对象

#浅拷贝 -- 浅拷贝就是快捷方式，深拷贝就是‘全备份’
import copy
print(disk)
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
#computer1和computer2是不同的，但所包含的子对象是相同的