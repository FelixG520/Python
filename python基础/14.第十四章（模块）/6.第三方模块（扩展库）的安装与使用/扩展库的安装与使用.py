# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！

'''
第三方模块的安装
pip install 模块名
第三方模块的使用
import 模块名
'''
import schedule
import time
#以schedul模块为例
def job():
    print('哈哈-----')

schedule.every(3).seconds.do(job)   #每隔三秒输出一遍
while True:
    schedule.run_pending()
    time.sleep(1)                   #休息一秒