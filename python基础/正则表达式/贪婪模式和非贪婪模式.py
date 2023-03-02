source ='<html><head><title>Title</title>'

import re
p = re.compile(r'<.*>')
print(p.findall(source))


p = re.compile(r'<.*?>')
print(p.findall(source))