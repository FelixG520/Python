# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
Python中的包
·Python中的包
  ·包是一个分层次的目录结构,它将一组功能相近的模块组织在一个目录下
  ·作用：
    ·代码规范
    ·避免模块名称冲突

  ·包与目录的区别
    ·Package是包，包含__init__.py文件的目录称为包
    ·Directory是目录，目录里通常不包含__init__文件
  ·包的导入
    import 包名.模块名
'''

#Directory是目录   ·目录里通常不包含__init__文件
#Package  是包    ·包含__init__.py文件的目录称为包


import Package1.module_A
print(Package1.module_A.a)   #这样写太长了

import Package1.module_A as ma  #ma是Package1.module_A这个模块的别名
print(ma.a)                     #这样写就简便多了