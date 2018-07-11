from sys import exit

def gold_room():
    """gold_room:input number"""
    print ("This room is full od gold. How much do you take?")

#    print ("int(next):{}" % int(next))
#    print ("next:%r" % next)
    choice = input(">")
    # if "0" in choice or "1" in choice:
#    if type(1) == type(int(next)):
    if choice.isdigit():
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print ("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    """bear_room:take honey/taunt bear/taunt bear/ open door"""
    print ("There is a bear here.")
    print ("The Bear has a bunch of honey.")
    print ("The fat bear is in front of another door.")
    print ("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print ("The bear has moved from the door.")
            print ("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print ("I got no ideas what that means.")


def cthulhu_room():
    """cthulhu_room:flee, head"""
    print ("Here you see the great evil Cthulhu.")
    print ("He, it, wharever stares at you and you go insane.")
    print ("Do you flee for your life or eat your head?")

    next = input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    """dead_why"""
    print (why, "Good jod!")
    exit(0)

def start():
    """start:left/right."""
    print ("You are in a dark room.")
    print ("There is a door to your right and left.")
    print ("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
       cthulhu_room()
    else:
       dead("You stumble around the room until you starve.");

#choice = int(input("input 1 to continue"))
#if next == 1:
#    print ("start~")
start()
#gold_room()
