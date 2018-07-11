i = 0
n = 6
numbers = []
while i < n:
    print (f"At the top i is {i}")
    numbers.append(i)

    i = i+1
    print ("Number now: ", numbers)
    print (f"At the bottom i is {i}")

def funct(n, t):
    i = 0
    while i < n:
        print (f"At the top i is {i}")
        numbers.append(i)
    
        i = i + t
        print ("Number now: ", numbers)
        print (f"At the bottom i is {i}")

print ("THe number: ")

#funct(8, 2)

for num in numbers:
    print (num)
