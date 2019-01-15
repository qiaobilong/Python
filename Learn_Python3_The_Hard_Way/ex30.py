people = 30
cars = 40
trucks = 15

if cars > people:
    print("车多")
elif cars < people:
    print("人多")
else:
    print("不确定")

if trucks > cars:
    print("货车多")
elif trucks < cars:
    print("货车少")
else:
    print("相等")

if people > trucks:
    print("人比货车多")
else:
    print("fine,let's stay home then.")
