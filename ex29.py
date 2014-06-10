

people = 20
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not too many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"

dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."

if people == dogs:
	print "People are dogs."

#Study drill questions:
##	1. What do you think the /if/ does to the code under it? 
## 	/if/ is a conditional operator, creating a 'branch' in the code.
##	2. Why does the code under the /if/ need to be intended four spaces?
## 	It must be intented in order to for it to be part of the conditional, it instucts the interpreter that this code is part of a larger code block.
##	3. What happens if it isn't intented?
## 	Conditional doesn't activate, syntax error.
##	4. Can you put other boolean expressions for Exercise 27 in the /if-statement/? Try it.
## 	Of course you can.
##	5. What happens if you change the initial variables for /people/, /cats/ and /dogs/?
##	Results of the conditional change e.g. some statements are not printed.