from sys import *

def dead(reason):
    print("u dead because %s") % reason

def choose():
    print "now u should choose one doors to go:"
    print "on your left  , it's a blue door"
    print "on your right , it's a red  door"
    print "so ,which door would u pull out?"
    do = int(raw_input("1. left \n2. right\n>"))
    if (do == 1):
        print "The door is opening~~"
        print "now , u see a snake(si ~ si ~) is protect the inside door.\n"
    elif (do == 2):
        print "The door is opening~~"
        print "it's a beer is sleeping behind an door(hum~zzZZ~~)"
    else:
        printf("what will you do")
        choose()

def light():
    do = int(raw_input("1. pick up fire \n2. go stright\n>"))
    if (do == 1):
        print "The house is light~~"
        print "now , u see the two doors in front of u.\n"
        choose()
    elif (do == 2):
        dead("u go stright and broken your head.")
    else:
        print("what will you do")
        light()

def start():
    print "Biu~ Dark and Dark ..."
    print "u are going to an house without light."
    print "what will you do?"
    light()

start()
