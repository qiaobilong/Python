# sys.exit 用于结束程序
from sys import exit

# 进入黄金房间后的逻辑
def gold_room():
    print("This room is full of gold. How much do you take?")

    # 如果输入不包含 0 或 1 则死
    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    # 如果输入的数字大于等于 50 则死
    if how_much < 50:
        print("Nice, you're not greedy, you  win!")
        exit(0)
    else:
        dead("You greedy bastard!")

# 实现熊房间的逻辑
def bear_room():
    print("There is a bear hear.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    # 如果熊离开后直接开门就用不到 while 循环了.
    while True:
        print("1.吃掉蜂蜜\n2.嘲笑熊\n3.打开门")
        next = input("> ")

        if next == "1":
            dead("熊看了看你，然后给了你一巴掌.")
        elif next == "2" and not bear_moved:
            print("熊已经从门口挪开了。你现在可以通过它了。")
            bear_moved = True
        elif next == "2" and bear_moved:
            dead("这次熊生气了，咬断了你的腿.")
        elif next == "3" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

# 恶魔房逻辑
def cthulhu_room():
    print("在这你看到了邪恶的Cthulhu.")
    print("他一直盯着你看.")
    print("你选择放弃还是被他吃掉你的头?")

    next = input("> ")

    # 二选一，否则恶魔放循环
    if "放弃" in next:
        start()
    elif "头" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

# 惨死函数
def dead(why):
    print(why, "Good job")
    exit(0)

# 启动函数
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

# 开始游戏
start()
