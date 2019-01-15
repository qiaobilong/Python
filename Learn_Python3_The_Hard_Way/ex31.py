print("你在一个小黑屋里，现在有两个门，输入1或者2打开其中一个门：")
door = input(">>>")

if door == "1":
    print("有个熊，在吃蛋糕")
    print("你该怎么做？")
    print("1.抢蛋糕吃")
    print("2.对着熊大叫")

    bear = input(">>>")

    if bear == "1":
        print("你是不是疯了！")
    elif bear == "2":
        print("食不言，寝不语，怎么学的！")
    else:
        print("你推陈出新的举动，救了你一命")
elif door == "2":
    print("2号门后面有啥，你还是去问原著吧")
else:
    print("告你输入1或2没，瞎输什么！！！")
