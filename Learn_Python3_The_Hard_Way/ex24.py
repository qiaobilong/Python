print("let's practice everything.")
print("you'd ennd to know 'bout escapes with \\ that do:")
print('\n newlines and \t tabs.')

poem = """
\tthe lovely world
with logic so firmly planted
看不懂，还是敲点中文吧\n还能练练打字
何乐而不为呐
\n\t\twhere there is none.
"""
print("-------------")
print(poem)
print("-------------")

five = 10-2+3-6
print(f"this should be five:{five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = int(jelly_beans / 1111)
    crates = jars / 100
    return jelly_beans,jars,crates

start_point = 10000
beans,jars,crates = secret_formula(start_point)
print(beans,jars,crates)
print("{:010.2f}".format(start_point))

formula = secret_formula(start_point)
print("{2}-{0}-{1}".format(*formula))
#可以回顾ex22.py
