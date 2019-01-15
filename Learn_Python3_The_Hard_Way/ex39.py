stuff = {'name' : 'qbl','age' : '26','sex' : '男' }

for a , b in list(stuff.items()):
    print(a,':',b)

state = stuff.get('qbl')
print(state)
if not state:
    print("sorry, no qbl")

state = stuff.get('qbl','不存在')
print(state)
