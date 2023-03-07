# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！
'''
1.什么叫模块_模块化编程的好处.编写程序文件，输入参考代码
[root@master ~]# vi /opt/software/data/project/p_19/p_19.py
2.按i键进入编辑模式，输入以下代码
按Esc键退出编辑模式，输入“:wq”保存退出
3.执行程序文件
[root@master ~]# python3 /opt/software/data/project/p_19/p_19.py
'''

#encoding=utf-8
def average_score(scores):
    # 统计平均分
    score_values = scores.values()
    sum_scores = sum(score_values)
    average = sum_scores / len(score_values)
    return average


def sorted_score(scores):
    # 对成绩从高到低排队.
    score_lst = [(scores[k], k) for k in scores]
    sort_lst = sorted(score_lst, reverse=True)
    return [(i[1], i[0]) for i in sort_lst]


def max_score(scores):
    # 成绩最高的姓名和分数.
    lst = sorted_score(scores)                # 引用分数排序的函数sorted_score
    max_score = lst[0][1]
    return [(i[0], i[1]) for i in lst if i[1] == max_score]

def min_score(scores):
    # 成绩最低的姓名和分数
    lst = sorted_score(scores)
    min_score = lst[len(lst) - 1][1]
    return [(i[0], i[1]) for i in lst if i[1] == min_score]

if __name__ == "__main__":
    examine_scores = {"李志": 95, "张红": 96, "黄和": 55, "胡杨": 85, "郑天": 50, "陈奇": 72, "刘海": 78, "姜红": 95, "王武": 95}
    ave = average_score(examine_scores)
    print("平均分是: ", ave)         #平均分
    sor = sorted_score(examine_scores)
    print("成绩表: ", sor)          #成绩表
    youxiu = max_score(examine_scores)
    print("最高分: ", youxiu  )     #成绩优秀者
    yiban = min_score(examine_scores)
    print("最低分: ", yiban  )      #成绩一般者