Directions = {'north', 'south', 'east', 'weast'}
Verbs = {'go', 'stop', 'kill', 'eat'}
Stop_words={ 'the', 'in', 'of', 'from', 'at', 'it'}
Nouns = {'door', 'bear', 'princess', 'cabinet'}

def __init__():
    pass  

def convert_number(word):
    try:
        return int(word)
    except ValueError:
        return None

def scan(sentense):
    last = []
    words = sentense.split(' ')
    for wod in words:
        ins = test_who(wod)
        last.extend([ins])
        #last.extend([test_who(word)])
    return last

def test_who(word):
    if word == None:
        return ('error','')
    if word in Directions:
        return ('direction',word)
    elif word in Verbs:
        return ('verb',word)
    elif word in Stop_words:
        return ('stop',word)
    elif word in Nouns:
        return ('noun',word)
    num = convert_number(word) 
    if num != None:
        return ('number',num)
    else:
        return ('error',word)

