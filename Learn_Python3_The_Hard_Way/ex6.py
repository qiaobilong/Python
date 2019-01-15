#给变量赋值
type_of_people = 10
#给x赋值一个字符串，并引用已有的变量
x = f"There are {type_of_people} type of people."
#给变量赋值
binary = "binary"
do_not = "don't"
y = f"those who now {binary} and those who {do_not}."
#打印x、y
print(x)
print(y)

print(f"i said: {x}")
#给字符串y加个单引号.当字符串中有单引号时，需要进行转义，或者使用双引号
print(f"i also said: '{y}'")
print(f'i also said: \'{y}\'')
print(f"i also said: “{y}”")#中英文有别

hilarious = False#关于布尔值，详见ex27.py
joke_evalustion = "isn't that joke so funny?! {}"
print(joke_evalustion.format(hilarious))#格式化字符串
#.format里的变量要大于joke_evalustion2里大括号的个数，否则会报错
print(">>>>>>>>>>>>>>>>>>>>>>>>")
true = True
joke_evalustion2 = "isn't that joke so funny?! {} {}"
print(joke_evalustion2.format(true,hilarious))

w = "this is the left side of..."
e = "a string with a right side."
print(w + e)
