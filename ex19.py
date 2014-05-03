#defines function 'cheese_and_crackers' to accept two arguemtns 'cheese_count' and 'boxes of crackers'
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#prints the string "You have %d cheeses!" where %d is replaced by the cheese_count argument given as a decimal.
	print "You have %d cheeses!" % cheese_count
	#prints the specified string with %d being replaced with boxes_of_crackers given as a decimal.
	print "You have %d boxes of crackers!" % boxes_of_crackers
	#prints the specified string.
	print "Man that's enough for a party!"
	#prints the specified string and begins a new line.
	print "Get a blanket.\n"
#lines 3 to 10 are indented 4 spaces (or tabbed) to make them part of function 'cheese_and_crackers'
	
#prints the string	
print "We can just give the function numbers directly:"
#runs function 'cheese_and_crackers' with '20' and '30' as given arguments.
cheese_and_crackers(20, 30)

#prints the string
print "OR, we can use variables from out script:"
#defines variable 'amount_of_cheese' as '10'
amount_of_cheese = 10
#defines variable 'amount_of_crackers' as '50'
amount_of_crackers = 50
#runs function 'cheese_and_crackers' with 'amount_of_cheese' and 'amount_of_crackers' as arguments.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#prints the string
print "We can even do maths inside too:"
#runs the function 'cheese_and_crackers' with the results of '10 + 20' and '5 + 6' as arguments.
cheese_and_crackers(10 + 20, 5 + 6)

#prints the string
print "And we can combine the two, variables and maths:"
#runs the function 'cheese_and_crackers' with the results of 'var$amount_of_cheese + 100' and 'var$amount_of_crackers + 1000'
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#mistake #1: line 9 invalid syntax. used a space instead of an underscore between 'and' and 'crackers'.
#mistake #2: line 13 invalid syntax. guess what?