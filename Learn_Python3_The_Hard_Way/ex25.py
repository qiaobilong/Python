def break_words(stuff):
    """切割字符串，split(分隔符，最多分隔次数)"""
    words = stuff.split()
    return words

def sort_words(words):
    """
    对可迭代对象进行排序，sorted(iterable,key,reverse = True),True降序，False升序，默认升序
    """
    return sorted(words)


def print_first_word(words):
    if type(words) == list:#if isinstance(words, (list)):
        word = words.pop(0)#移除列表中的一个元素（默认最后一个），返回该值
        print("list")
    else:
        word = list(words).pop(0)#移除列表中的一个元素（默认最后一个），返回该值
        print("str")
    print(word)

def print_last_word(words):
    if isinstance(words, (list)):
        word = words.pop(-1)#移除列表中的一个元素（默认最后一个），返回该值
    else:
        word = list(words).pop(-1)#移除列表中的一个元素（默认最后一个），返回该值
    print(word)

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
