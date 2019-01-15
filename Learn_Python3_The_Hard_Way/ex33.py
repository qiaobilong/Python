i = 0
numbers = []

while i < 6:
    print(f"at the top i is {i}")
    numbers.append(i)
    i = i + 1
    print(f"numbers now {numbers}")
    print(f"at the bottom i is {i}\n")

print("the numbers:")
for i in numbers:
    print(i)
