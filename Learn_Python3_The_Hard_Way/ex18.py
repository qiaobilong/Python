#*是把所有参数都接收进来，放到args的列表中
def print_two(*args):
    arg1, arg2,arg3 = args
    print(f"arg1: {arg1},arg2: {arg2},arg3: {arg3}")
#传入的参数个数必须和函数能接收的参数相等，否则会报错
print_two("qbl","qqq","bbb")

def print_two_again(arg1,arg2):
    print(f"arg1: {arg1},arg2: {arg2}")
print_two_again("qbl","qqq")

def print_one(arg1):
    print(f"arg1: {arg1}")
print_one("qbl")

def print_none():
    print("i got nothin.")
print_none()
 
