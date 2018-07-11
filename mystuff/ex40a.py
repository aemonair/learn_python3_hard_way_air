import mystuff

mystuff.apple()
print (mystuff.tangerine)

mystuff1 = {'apple': "I AM APPLES!"}
mystuff1['apple']    # get apple from dict
print (mystuff1['apple'])
mystuff.apple()     # get apple from the module
mystuff.tangerine   # same thing, it's just a variable
print (mystuff.tangerine)

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print ("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple()
print (thing.tangerine)
