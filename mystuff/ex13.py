from sys import argv

#script, first, second, third =  argv

#print "The script is called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third

run, v1, v2 = argv
#v1 = raw_input()
print "program:" , run
print "var1:" + v1
print "var2:" + v2
v1 = raw_input("var1_input:")
v2 = raw_input("var2_input:")
print "var1:" + v1
print "var2:" + v2
