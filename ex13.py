from sys import argv

script, first, second, third = argv

print "The script is called", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print "What variable do you like most?"
fav_variable = raw_input()
print "So, your favourite variable is %s" % (fav_variable)