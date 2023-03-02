source ='''苹果，苹果是绿色的
橙子，橙子是橙色的
香蕉，香蕉是黄色的
'''

import re
p = re.compile(r'^(.*)，',re.MULTILINE)
for one in p.findall(source):
    print(one)


source2 ='''张三，手机号码15945678981
李四，手机号码13945677701
王二，手机号码13845666901
'''

p = re.compile(r'^(.+)，.+(\d{11})',re.MULTILINE)
for one in p.findall(source2):
    print(one)
