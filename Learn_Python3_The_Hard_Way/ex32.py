the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
    print(f"this is count {number}")

for fruit in fruits:
    print(f"a fruit of type {fruit}")

for i in change:
    print(f"i got {i}")

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
elements = []

def print_list(lists):
    print(lists)
    for i in lists:
        print(f"element was: {i}")

for i in range(0,6,2):
    #range(start, stop[, step])
    print(i)
    elements.append(i)
print_list(elements)

elements.insert(1,88)
print_list(elements)

"""列表操作：https://www.cnblogs.com/cnhkzyy/p/7643244.html
append/extend合并/insert插入/del/pop/remove/sort排序原列表/sorted排序生成一个新列表
"""
