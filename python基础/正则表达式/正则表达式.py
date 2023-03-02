
content='''
Python3 高级开发工程师 上海互教教育科技有限公司上海-浦东新区2万/月02-18满员
测试开发工程师(C++/python) 上海墨数码科技有限公司上海-浦东新区2.5万/每月02-18未满员
Python3 开发工程师 上海德拓信息技术股份有限公司上海-徐汇区1.3万/每月02-18剩余11人
测试开发工程师 (Python) 赫里普 (上海)信息科技有限公司上海-浦东新区1.1万/每月02-18剩余5人
Python高级开发工程师 上海行动教育科技股份有限公司上海-闵行区2.8万/月2-18剩余255人
python开发工程师 上海优似腾软件开发有限公司上海-浦东新区2.5万/每月02-18满员'''

import re
#compile函数的参数，就是正则表达式字符串
p = re.compile(r'([\d.]+)万/每{0,1}月')#\d表示数字，{0，1}表示”每“可以出现0次也可以出现一次
for one in p.findall(content):
    print(one)

content='''
苹果是绿色的
橙子是橙色的
香蕉是黄色的
乌鸦是黑色的
'''
p = re.compile(r'.色')
for one in p.findall(content):
    print(one)