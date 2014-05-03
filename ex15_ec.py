#imports the command line argument variable module
from sys import argv
#defines 'script' as the argument variable
script = argv
#asks user for filename input
print "Hello you. What file would you like to display?"
filename = raw_input("\[T]/ ")
#opens the file specified in the command line parameters.
txt = open(filename)
#prints a notification of what file was selected.
print "Here's your file %r:" % filename
#prints the content of the opened file.
print txt.read()
txt.close()
print "File closed. Script ending..."