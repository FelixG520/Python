import re
content='''
苹果，是绿色的
橙子，是橙色的
香蕉，是黄色的
乌鸦，是黑色的
猴子，
'''
p = re.compile(r'，.*')
for one in p.findall(content):
    print(one)