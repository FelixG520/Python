source ='''
苹果.是绿色的
橙子.是橙色的
香蕉.是黄色的'''

import re
p = re.compile(r'<.*\.>')
print(p.findall(source))


