Directions = {'north', 'south', 'east', 'weast'}
Verbs = {'go', 'stop', 'kill', 'eat'}
Stop_words={ 'the', 'in', 'of', 'from', 'at', 'it'}
Nouns = {'door', 'bear', 'princess', 'cabinet'}

class ex48_scan(object):
    def __init__(self):
        return

    def convert_number(self, word):
        try:
            return int(word)
        except ValueError:
            return None
    
    def scan(self, sentense):
        last = []
        words = sentense.split(' ')
        print ("Word:", words)
        for word in words:
            print ("test_who:", self.test_who(word))
            ins = ()
            ins = self.test_who(word)
            last.extend([ins])
            print ("last:",last)
            #last.append(test_who(word))
            #last.extend([test_who(word)])
        return last
    
    def test_who(self, word):
        if word in Directions:
            return ('direction',word)
        elif word in Verbs:
            return ('verb',word)
        elif word in Stop_words:
            return ('stop',word)
        elif word in Nouns:
            return ('noun',word)
        num = self.convert_number(word) 
        if num:
            return ('number',num)
        else:
            return ('error',word)

ex48_test = ex48_scan()
last = ex48_test.scan("go eat the cabinet")
print (last)
print ("--------------------")
last = ex48_test.scan("north")
print (last)
print ("--------------------")
last = ex48_test.scan("north south east")
print (last)
print ("--------------------")
last = ex48_test.scan("go")
print (last)
print ("--------------------")
last = ex48_test.scan("go kill eat")
print (last)
print ("--------------------")
last = ex48_test.scan("the")
print (last)
print ("--------------------")
last = ex48_test.scan("the in of")
print (last)
print ("--------------------")
last = ex48_test.scan("bear")
print (last)
print ("--------------------")
last = ex48_test.scan("bear princess")
print (last)
print ("--------------------")
last = ex48_test.scan("1234")
print (last)
print ("--------------------")
last = ex48_test.scan("3 91234 456")
print (last)
print ("--------------------")
last = ex48_test.scan("ASDFADFASDF")
print (last)
print ("--------------------")
last = ex48_test.scan("bear IAS princess")
print (last)
print ("--------------------")
