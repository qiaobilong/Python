from sys import argv
from os.path import exists

script , from_file, to_file = argv

print(f"复制 {from_file} to {to_file}")
#打开源文件
in_file = open(from_file)
#读取源文件
indata = in_file.read()
print(f"the input file is {len(indata)} bytes long")
#exists:文件存在返回True，否则返回False
print(f"does the output file exist? {exists(to_file)},{exists(from_file)}")
#打开目标文件
out_file = open(to_file,'w')
#写入数据
out_file.write(indata)
#关闭目标文件
out_file.close()
#关闭源文件
in_file.close()
