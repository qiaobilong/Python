from sys import argv
script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count,f.readline())

def close(f):
    f.close()

current_file = open(input_file)

print(">>>>>>>>>>>>>>>>")
print_all(current_file)

print(">>>>>>>>>>>>>>>>")
rewind(current_file)

current_line = 1
print_a_line(current_line,current_file)

rewind(current_file)
print_a_line(current_line,current_file)
current_line += 1
print_a_line(current_line,current_file)

close(current_file)
