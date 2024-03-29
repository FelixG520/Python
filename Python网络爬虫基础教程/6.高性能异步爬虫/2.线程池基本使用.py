# import time
# #使用单线程串行方式执行
#
# def get_page(str):
#     print("正在下载 ：",str)
#     time.sleep(2)
#     print('下载成功：',str)
#
# name_list =['xiaozi','aa','bb','cc']
#
# start_time = time.time()
#
# for i in range(len(name_list)):
#     get_page(name_list[i])
#
# end_time = time.time()
# print('%d second'% (end_time-start_time))



import time
#导入线程池模块对应的类
from multiprocessing.dummy import Pool #应用在阻塞程序
#使用线程池方式执行
start_time = time.time()
def get_page(str):
    print("正在下载 ：",str)
    time.sleep(2)
    print('下载成功：',str)

name_list =['xiaozi','aa','bb','cc']

#实例化一个线程池对象
pool = Pool(4) #四个线程处理四个阻塞操作
#将列表中每一个列表元素传递给get_page进行处理。
pool.map(get_page,name_list)
pool.close()
pool.join()
end_time = time.time()
print(end_time-start_time)



