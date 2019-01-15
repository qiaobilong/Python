#主函数
def main():
    print("1.春季\n2.夏季\n3.秋季\n4.冬季")
    season = input(">>>")
    if season == "1":
        spring()
    elif season == "2":
        summer()
    elif season == "3":
        autumn()
    elif season == "4":
        winter()
    else:
        print("请输入季节对应的编号：")
        main()
#春季
def spring():
    print("春天风大，不好，你还是选一个别的季节吧：")
    main()

def summer():
    print("你为什么会选择夏季，请给我一个合理的理由：")
    condition = True

    while condition:
        print("1.暖和\n2.有西瓜吃")
        reason = input(">>>")

        if reason == "1":
            print("热不死你，重选：")
            condition = False
            main()
        elif reason == "2":
            print("你个吃货，重选：")
            condition = False
            main()
        else:
            print("请输入对应编号，你还有点规矩没了！！！")

def autumn():
    print("秋天是个收获的季节，但你不觉得这个季节有点凄凉吗？常言道：“秋风扫落叶”，我建议你还是换个季节吧。")
    main()

def winter():
    print("这么巧，你也喜欢冬季啊，我感觉我们太有缘了！")
    print("恭喜你闯关成功，享受即将到来的寒冷吧^_^")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n是不是很无聊，我写的时候更无聊")

#启动函数
def start():
    print("----------------------欢迎来到无聊小游戏----------------------")
    print("首先请输入你最喜欢的一个季节：")
    main()

#开始游戏
start()
