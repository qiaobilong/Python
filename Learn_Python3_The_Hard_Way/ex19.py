def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"you have {cheese_count} cheeses!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("man that's enough for a party!")
    print("get a blanket.\n")

print(">>>>>>>>>>>>>")
cheese_and_crackers(20,30)

print(">>>>>>>>>>>>>")
amount_fo_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_fo_cheese,amount_of_crackers)

print(">>>>>>>>>>>>>")
cheese_and_crackers(10 + 20, 5 + 6)

print(">>>>>>>>>>>>>")
cheese_and_crackers(amount_fo_cheese + 100, amount_of_crackers + 1000)

print(">>>>>>>>>>>>>")
in1 = input("请输入奶酪的数量:")
in2 = input("请输入薄脆饼干的数量:")
cheese_and_crackers(in1,in2)
