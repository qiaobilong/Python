lists = [1,2,3,4,5]

def my_list(lists):
    for i in range(len(lists)):
        print(f"index:{i} - ",end = "")
        print(lists[i])
    pass
my_list(lists)
