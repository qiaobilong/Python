n = 3
print("\n" * n)
formatter = "{} {} {} {}"
print(formatter.format(1,
2,
3,
4,
5))
ft = formatter.format(11,12,13,14)
print(type(1))
print(ft)
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,True,False))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format("try your","own text here","maybe a poem","or a song about fear"))
