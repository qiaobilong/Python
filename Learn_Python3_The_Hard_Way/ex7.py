n = 2
print("\n" * n)

print("mary had a little lamb.")
print("its fleece was white as {}.".format('snow'))

#扩展学习.format
print("my name is {},age {}.".format("Zerone龍",26))

print(">>>>>>>>>>>列表：'*list'")
list = [26,"'Zerone龍'"]
print("my name is {},age {}".format(*list))
print(">>>>>>>>>>>>>也可自定义顺序")
print("my name is {1},age {0},{1} is alias.".format(*list))
print(">>>>>>>>不使用变量")
print("my name is {},age {}".format("Zerone龍",26))

print(">>>>>>>>字典：'**dicts'")
print("my name is {name},age {age}.".format(age = 26,name = "Zerone龍"))
dicts = {"name":"Zerone龍","age":26}
print("my name is {name},age {age}.".format(**dicts))
#扩展学习.format完

print("and everywhere that mary went.")
print("." * 10)

end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6,end = ' ')#end default换行
print(end7 + end8 + end9 + end10 + end11 +end12,end = ' ')
print(end1,end2,end3,end4,end5,end6,sep = '')#sep指定每个变量间的连接符，default空格
