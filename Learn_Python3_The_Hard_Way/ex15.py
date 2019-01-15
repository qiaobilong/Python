from sys import argv

script,filename = argv

txt = open(filename)

print(f"here's your file {filename}:")
print(txt.read())
txt.close()

print("type the filename again:")
file_again = input(">")
#+读写
txt_again = open(file_again,'r+')
print(txt_again.readline())
txt_again.close()
