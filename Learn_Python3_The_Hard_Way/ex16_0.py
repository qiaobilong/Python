from sys import argv

script,filename = argv
#'r+'读写，无文件，报错;覆盖写（long → 12ng）
#'w+'读写，无文件，新建;清空写（long → 12）
#'a+'读写，无文件，新建;追加写（long → long12）
fo = open(filename,'r+')
fo.write(input('请写入：'))

#与fo.close()类似
fo.flush()

#1.再次读取文件内容，可以再次执行open将指针移至开头
print(open(filename).read())
open(filename).close()
#2.也可以使用seek将指针移至开头
##seek(offset[, whence]) ，offset是相对于某个位置的偏移量;
##要用'b模式'打开，例如'rb'
##位置由whence决定，默认whence=0，从开头起；whence=1，从当前位置算起；
##whence=2相对于文件末尾移动，通常offset取负值
fo.seek(0)
print(fo.read())
fo.close()
