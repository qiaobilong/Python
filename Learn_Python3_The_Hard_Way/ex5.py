name = 'qbl'
age = 26
height = 74*2.54 #英寸转厘米
weight = 172*0.4535924 #磅转千克
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print(f"let's talk about {name}")
print(f"he's {round(height,2)} inches tall")
print(f"he's {weight} pounds heavy.")
print("actually that's not too heavy")
print(f"he's got {eyes} eyes and {hair} hair")
print(f"his teeth are usually {teeth} depending on the coffee")

#this line is tricky , try to gei it exactly right
total = age + height + weight
print(f"if i add {age},{height},and {weight} i get {total}")
