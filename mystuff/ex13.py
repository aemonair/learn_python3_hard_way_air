from sys import argv
# read the WYSS section for how to run this
script, first, second, third =  argv

print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)

run, v1, v2, v3 = argv
v1 = input()
print ("program:" , run)
print ("var1:" , v1)
print ("var2:" , v2)
v1 = input("var1_input:")
v2 = input("var2_input:")
print ("var1:" , v1)
print ("var2:" , v2)
