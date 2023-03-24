#5、请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续 判断第二个字母。
day=input("请输入第一个字母：")
day=day.upper()
if day == "M":
    print("是星期一")
elif day == "W":
    print("是星期三")
elif day == "F":
    print("是星期五")
elif day == "T":
    a=input("请输入第二个字母：")
    if a == "u":
        print("这是星期二")
    elif a == "h":
        print("这是星期四")
elif day == "S":
    a=input("请输入第二个字母：")
    if a == "u":
        print("这是星期日")
    elif a == "a":
        print("这是星期六")
