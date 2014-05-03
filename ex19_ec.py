import math
def hardmaths(bignumber1, bignumber2):
	print "\nWe're gonna do some hard maths!"
	print "Your first number was %d." % (bignumber1)
	print "Your second number was %d." % (bignumber2)
	print "Let's do some hard maths!"
	print "%d is the product of your two numbers." % (bignumber1 * bignumber2)
	print "%f is the square root of your second number." % (math.sqrt(bignumber2))
	print "%f is the base-10 logarithm of your first number.\n" % (math.log10(bignumber1))
	
print "\nMaths time. I need two numbers. 6 digits minimum. Integers only\n"
big1 = int(raw_input("> "))
big2 = int(raw_input("> "))

hardmaths(big1, big2)

print "Okay, that was pretty huge. How about another trick? Just one integer please.\n"
big3 = int(raw_input("> "))

hardmaths((big3 * big3), (big3 + (big3 / big3)))

#but seriously fuck putting trying to do clever things 10 fucking times with functions.