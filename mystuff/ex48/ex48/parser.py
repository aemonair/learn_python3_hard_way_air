class ParserError(Exception):
    pass

class Sentence(object):
    def __init__(self, subject, verb, obj):
        """Init 初始化 Sentence 句子"""
        # remember we take ('noun','princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

def peek(word_list):
    """peek 窥视 查看word的类型"""
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    """match 匹配 是否为 expecting 类型"""
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    """ Skip 跳过 word_type 类型 """
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    """parse 语法分析 verb 动词"""
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    """parse 语法分析 object 名词/方向"""
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
    """parse 语法分析 object 名词/方向"""
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match (word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
