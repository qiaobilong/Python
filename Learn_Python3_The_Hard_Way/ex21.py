def add(a,b):
    print(f"{a} + {b} = ",end = "")
    return a + b
def subtract(a,b):
    print(f"{a} - {b} = ",end = "")
    return a - b
def multiply(a, b):
    print(f"{a} * {b} = ",end = "")
    return a * b
def divide(a,b):
    print(f"{a} / {b} = ",end = "")
    return a / b

operation = int(input("0：加法\n1：减法\n2：乘法\n3：除法\n请输入运算编号："))
num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))

if operation == 0:
    adds = add(num1,num2)
    print(adds)
elif operation == 1:
    subtracts = subtract(num1,num2)
    print(subtracts)
elif operation == 2:
    multiplys = multiply(num1,num2)
    print(multiplys)
elif operation == 3:
    divides = divide(num1,num2)
    print(divides)
