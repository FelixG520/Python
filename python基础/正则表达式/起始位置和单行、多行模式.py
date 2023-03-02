source ='''001-苹果价格-60
002-橙子价格-70
003-香蕉价格-80
'''

import re
p = re.compile(r'^\d+',re.M) #re.多行模式
for one in p.findall(source):
    print(p.findall(source))



p = re.compile(r'\d+$',re.M) #re.多行模式
for one in p.findall(source):
    print(p.findall(source))