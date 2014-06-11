i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num

# Study drills.
# 1. Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable.
# 2. Now use this function to rewrite the script to try different numbers.
# 3. Add another variable to the function arguments that you can pass in that lets you change the + 1 on line 8 so you can change how much it increments by.
# 4. Rewrite the script again to use this function to see what effect that has.
# 5. Now, write it to use for-loops and range instead. Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?

# SD 1.

print "\nConverting while-loop to function, drill_1"

def drill_1(n):
	i = 0
	numbers1 = []
	while i < n:
		print "Item %d" % i
		numbers1.append(i)
		i = i + 1
	print numbers1

# SD 2.

print "\nUsing drill_1 with n = 3"
drill_1(3)

print "\nUsing drill_1 with n = 8"
drill_1(8)

# SD 3.

print "\nCreating function drill_3 to allow variable step size."
# With lists (Python arrays) we want to control the /start/, /stop/ and /step/ values.
def drill_3(n, s):
	# n is the length of the list, s is the step size.
	i = 0
	numbers3 = []
	while i < n:
		print "Item: %d" % i
		numbers3.append(i)
		i = i + s
	print numbers3

# SD 4.

print "\nUsing drill_3 with n = 12 and s = 3"
drill_3(12, 3)

# SD 5.

print "\ndrill_5 uses a for-loop and range instead."
def drill_5 (n, s):
	numbers5 = range(0, n, s)
	# We have to specify 0 as a starting point so Python
	# reads the other elements correctly (otherwise it
	# just interprets n and s as /stop/ and /start/).
	for i in numbers5:
		print "Item %d" % i
	print numbers5

drill_5(14, 4)