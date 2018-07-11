import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
        "class %%%(%%%):":
          "Make a class named %%% that is-a %%%.",
        "class %%%(object):\n\tdef __init__(self, ***)":
          "class %%% has-a __init__ that takes self and *** parameter",
        "class %%%(object):\n\tdef ***(self, @@@)":
          "class %%% has-a function *** that takes self and @@@ parameter",
        "*** = %%%()":
          "Set *** to an instance of class %%%.",
        "***.***(@@@)":
          "From *** get the *** function, call it with params self.@@@",
        "***,*** = '***'":
          "From *** get the *** attribute and set it to '***'."
          }
# do they want to drill phrases first
if (len(sys.argv) == 2 and sys.argv[1] == "english"):
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

print (PHRASE_FIRST)

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))
print(33, WORDS)    

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in 
                   random.sample(WORDS, snippet.count("%%%"))]
    print (38, class_names)
    input ("> ")
    other_names = random.sample(WORDS, snippet.count("***")) 
    print (41, other_names)

    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        print (54, result)
        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        #fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        #fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        print (67, result)
        results.append(result)    
    
    print (70, results)
    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        print (77, snippets)
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            print (82, snippet)
            print (83, phrase)
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print (88, question)    

            input ("> ")
            print (f"ANSWER: {answer}\n\n")
            input ("> ")
except EOFError:
    print ("\nBye")
