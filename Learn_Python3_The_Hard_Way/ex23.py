import sys
script,encoding,error = sys.argv


def main(language_file,encoding,errors):
    line = language_file.readline()

    if line:
        print_line(line,encoding,errors)
        return main(language_file,encoding,errors)


def print_line(line,encoding,errors):
    next_lang = line.strip()#strip去除头尾特定字符，默认空格/换行符（此处用于去掉每行的"\n"）
    raw_bytes = next_lang.encode(encoding,errors = errors)#encode编码
    cooked_srting = raw_bytes.decode(encoding,errors = errors)#decode解码
    #字节串<===>字符串
    print(raw_bytes,"<===>",cooked_srting)


languages = open("languages.txt",encoding = "utf-8")

main(languages,encoding,error)

"""
编码问题,转：https://blog.csdn.net/gqtcgq/article/details/47068817
"""
