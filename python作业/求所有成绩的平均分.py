'''Python程序设计作业4

练习、选择结构、循环结构
注意：要求把代码和运行结果贴在作业里

目的：
1.什么叫模块_模块化编程的好处、熟练选择结构编程、循环结构编程。
2、理解选择结构、循环结构。
内容：
1.什么叫模块_模块化编程的好处、编写程序，输入若干个成绩，求所有成绩的平均分。每输入一个成绩后询问是否继续输入下一个成绩，回答“yes”就继续输入下一个成绩，回答“no”就停止输入成绩。

提示：采用循环结构 + 异常处理结构来保证用户输入的合法性。

'''

numbers = []  # 使用列表存放临时数据
while True:
    x = input('请输入一个成绩：')
    try:  # 异常处理结构
        numbers.append(float(x))
    except:
        print('不是合法成绩')
    while True:
        flag = input('继续输入吗？（yes/no）').lower()
        if flag not in ('yes', 'no'):  # 限定用户输入内容必须为yes或no
            print('只能输入yes或no')
        else:
            break
    if flag == 'no':
        break

print(sum(numbers) / len(numbers))





