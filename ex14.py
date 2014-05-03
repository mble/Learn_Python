from sys import argv

script, user_name, difficulty = argv
prompt ='\[T]/ '
#prompt ='> '

print "You have selected: %s MODE." %(difficulty.upper())
print "Hi %s, I'm the %s script." %(user_name, script)
print "I'd like to ask you a few questions."
print "Do you praise the sun, %s?" % user_name
praise = raw_input(prompt)

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of blade do you have?"
blade = raw_input(prompt)

print '''
You fool, you selected %s MODE! Therefore:
You said %r about praising the sun.
You live in %r. Not sure where that is.
And you have a %r blade. Nice.
''' % (difficulty.upper(), praise, lives, blade)

#Mistake #1: misspelt argv as 'argb'.

#\[T]/ ~If only I could be so grossly incandescent.