# 我想大部分人都知道，通常一个程序员会具有的美德。当然了，有三种：懒惰、暴躁、傲慢。
# 一个人写的烂软件将会给另一个人带来一份全职工作。
# 一鼓作气，考研是一种忍耐！！！


lst=[{'rating':[9.7,2062397],'id':'1292052','type':['犯罪','剧情'],'title':'肖申克的教赎','actors':['蒂蝴.罗宾斯','摩根,弗里曼']},
     {'rating':[9.6,1528760],'id':'1291546','type':['剧情','爱情','同性'],'title':'霸王别姬','actors':['张国荣','张丰毅','巩俐','葛优']},
     {'rating':[9.5,1559181],'id':'1292720','type':['剧情','爱情'],'title':'阿甘正传','actors':['汤姆·汉克斯','罗宾·怀特']}
     ]




print('---------使用“#”暂时注释部分代码-----------')
name = input('请输入你要查询的演员：')
for item in lst:  # 遍历列表-->{}   item是一个又一个字典
    for movie in item:  # 遍历字典，得到movie是一个字典中的key
        print(movie)
    print('------------------------------')

    '''actors=movie['actors']

        if name in actors:
         print(name='出演了:'+movie)
    '''



name = input('请输入你要查询的演员：')
for item in lst:  # 遍历列表-->{}   item是一个又一个字典
    act_lst=item['actors']
    print(act_lst)


name = input('请输入你要查询的演员：')
for item in lst:  # 遍历列表-->{}   item是一个又一个字典
    act_lst=item['actors']
    for actor in act_lst:
        if name in actor:
            print(name,'出演了',item['title'])