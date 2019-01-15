ten_things = "苹果 鸭梨 香蕉 西瓜 火龙果"

print("不够10个，把他补全")
stuff = ten_things.split()
print(stuff)
more_stuff = ["蓝莓","桃","香瓜","枣","葡萄"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding:",next_one)
    stuff.append(next_one)
    print(f"加完后长度为：{len(stuff)}")

print(">>>>>>>>>>>>>>>>>>>>")
print(stuff)
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
