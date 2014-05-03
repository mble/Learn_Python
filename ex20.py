from sys import argv #from module sys, import function argv (array of arguments passed to script)

script, input_file = argv #define array as script, then input_file, in that order.

def print_all(f): #defines the function 'print_all' with parameter 'f' for file.
	print f.read() #prints the whole file.
	
def rewind(f): #defines the function 'rewind' with parameter 'f' for file.
	f.seek(0) #seeks to beginning of the file.

def print_a_line(line_count, f): #defines the function 'print_a_line' with parameters 'line_count' then 'f'
	print line_count, f.readline() #prints the line count of the file, follows by the specified line in the file.

current_file = open(input_file) #defines variable 'current_file' as the opened file specified in the command line argument (var input_file).

print "\nFirst let's print the whole file:\n" #prints the specified string.

print_all(current_file) #runs the print_all function on the current file

print "Now let's rewind, kind of like a tape.\n" #prints the specified string

rewind(current_file) #runs the rewind function on the current file

print "Let's print three lines:\n" #prints the specified string

current_line = 1 #defines the variable current_line as '1'
print_a_line(current_line, current_file) #runs the print_a_line function with the current line and current file as arguments. [Currently = 1] we have to define using = before using += for obvious reasons

current_line += 1 #defines the current_line variable as itself + 1
print_a_line(current_line, current_file) #runs the print_a_line function with the current line and current file as arguments. [Currently = 2]

current_line += 1 #defines the current_line variable as itself + 1
print_a_line(current_line, current_file) #runs the print_a_line function with the current line and current file as arguments. [Currently = 3]

#mistake #1: line 26, mispelled 'current'.

