#定义扑克序列
poker_list = []
for i in range(52):
    poker_list.append(i)
print(poker_list)

#定义花色
poker_color = []
for i in range(52):
    poker_color.append(i % 4)

    if poker_color[i] == 0:
        poker_color[i] = "红桃"
    elif poker_color[i] == 1:
        poker_color[i] = "方块"
    elif poker_color[i] == 2:
        poker_color[i] = "梅花"
    elif poker_color[i] == 3:
        poker_color[i] = "黑桃"
    else:
        print("花色有问题！！！")

print(poker_color)

#定义扑克数值
poker_number = []
for i in range(52):
    poker_number.append(int(i / 4))
print(poker_number)
