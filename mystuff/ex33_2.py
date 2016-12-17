i = 0
numbers = []

for i in range(6):
    print "At the top i is %d" % i
    numbers.append(i)
    print "Numbers now: %r" % numbers    
    i = i+1
    print "At the bottom i is %d" % i


print "The numbers: "
for num in numbers:
    print num
