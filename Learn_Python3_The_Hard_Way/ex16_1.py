from sys import argv
script , filename = argv
print(f"we're going to erase {filename}")
#用户中断执行(通常是输入了ctrl-c)，异常名称：KeyboardInterrupt
print("if you don't want that , hit ctrl-c (^c)")
print("if you do want that , hit return")
#等待用户判断
input("?")
#打开文件
fo = open(filename,'w')
#清空内容
fo.truncate()
#输入三行数据
line1 = input('line1:')
line2 = input('line2:')
line3 = input('line3:')
#定义换行变量
nl = '\n'
#写入数据
fo.write(line1 + nl + line2 + nl + line3 + nl)
#关闭文件
fo.close()
