#my_name = 'Zed A. Shaw'
#my_age = 35 # not a lie
#my_height = 74 #inches
#my_weight = 180 #lbs
#my_eyes = 'blue'
#my_teeth = 'White'
#my_hair = 'Brown'

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'blue'
teeth = 'White'
hair = 'Brown'

#print "Let's talk about %s." % my_name
#print "He's %d inches tall." % my_height
#print "He's %d pounds heavy." % my_weight
#print "Actually that's not too heavy."
#print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
#print "His teeth are usually %s depending on the cofffee." % my_teeth

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the cofffee." % teeth
#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
        #my_age, my_height, my_weight, my_age + my_weight + my_height)
        age, height, weight, age + weight + height)


print "%r ~~ %s `` %d" % ('\n', '\n', 34)
print "%r -- %s ++ %d" % ('\r', '\r', 34)
