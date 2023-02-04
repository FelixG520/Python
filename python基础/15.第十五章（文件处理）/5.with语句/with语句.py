#coding=gbk
'''
with语句(上下文管理器
with语句可以自动管理上下文资源，不论什么原因跳出with块都能确保文件正确的关闭，以此来达到释放资源的目的
'''

print(type(open('a.data','r')))
with open('a.data','r') as file:#open('a.data','r')这句话的对象就是上下文管理器
    print(file.read())

#不用写close()了，当离开with语句时，自动释放资源


with open('中分.jpg','rb') as src_file:
    with open('copy.png','wb') as target_file:
        target_file.write(src_file.read())