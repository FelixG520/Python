# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
1.什么叫模块_模块化编程的好处、在命令提示符环境使用命令安装扩展库python-docx。
[root@master ~]#pip3 install /opt/software/lxml-4.5.2-cp36-cp36m-manylinux1_x86_64.whl
[root@master ~]#pip3 install /opt/software/python-docx-0.8.9.tar.gz

2、查看测试文档（其中一行是红色字体，一行是加粗字体，一行是红色且加粗字体，另外二行是黑色字体）
[root@master ~]# ll /opt/software/data/project/p_11/test.docx
3、编写程序
[root@master ~]# vi /opt/software/data/project/p_11/p_11.py
4、按i键进入编辑模式，输入以下代码
修改完成后按Esc键退出编辑模式，输入“:wq”保存退出文档
5、执行程序
[root@master ~]# cd /opt/software/data/project/p_11
[root@master p_11]# python3 /opt/software/data/project/p_11/p_11.py
'''

#encoding=utf-8
from docx import Document
from docx.shared import RGBColor
boldText = []
redText = []
#获取文档对象
doc = Document("test.docx")
for p in doc.paragraphs:
    for r in p.runs:
        # 加粗字体
        if r.bold:
            boldText.append(r.text)
        # 红色字体
        if r.font.color.rgb == RGBColor(255, 0, 0):
            redText.append(r.text)
result = {'red text': redText,'bold text': boldText,'both': set(redText) & set(boldText)}

# 输出结果
for title in result.keys():
    print(title.center(30, '='))
for text in result[title]:
    print(text)
