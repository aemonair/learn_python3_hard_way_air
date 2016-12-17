numbers = []

def func(n):
    i = 0
    while i < n:
        print "At the top i is %d" % i
        numbers.append(i)
    
        i = i+1
        print "Number now: ", numbers
        print "At the bottom i is %d" % i

def funct(n, t):
    i = 0
    while i < n:
        print "At the top i is %d" % i
        numbers.append(i)
    
        i = i + t
        print "Number now: ", numbers
        print "At the bottom i is %d" % i
print "THe number: "

#funct(8, 2)

for num in numbers:
    print num
