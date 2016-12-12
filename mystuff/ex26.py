import ex25

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):# found 1:
    """Prints the first word after popping it off."""
    #word = words.poop(0) #found 11
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)#found 2 )
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

#found 9 five = 10 - 2 + 3 - 5
five = 10 - 2 + 3 - 6 
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    #found 3 jars = jelly_beans \ 1000
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
#found 8 beans, jars, crates == secret_formula(start-point)
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
#print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont)# found 4 )
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)# found 10 )


sentence = "All god\tthings come to those who weight."

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
#found 5 .print_first_word(sorted_words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
#found 6 prin sorted_words
print sorted_words

#print_irst_and_last(sentence) # found 12
print_first_and_last(sentence)

#   print_first_a_last_sorted(senence) # found 7
#print_first_a_last_sorted(senence) # found 13
#print_first_and_last_sorted(senence)#found 14
print_first_and_last_sorted(sentence)
