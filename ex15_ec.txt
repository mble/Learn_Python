#imports the command line argument variable module
from sys import argv
#defines 'script' and 'filename' as the argument variables
script, filename = argv
#opens the file specified in the command line parameters.
txt = open(filename)
#prints a notification of what file was selected.
print "Here's your file %r:" % filename
#prints the content of the opened file.
print txt.read()
#prints the specified string.
print "Type the filename again:"
#defines the variable 'file_again' as what the raw_input is.
file_again = raw_input("> ")
#defines the variable 'txt_again' as result of the open function and the 'file_again' variable.
txt_again = open(file_again)
#prints the content of the opened file.
print txt_again.read()