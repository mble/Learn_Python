from sys import argv

script, filename = argv

print "We're going erase %r." %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "File truncated. Praise the sun! \[T]/"
target.truncate()

print "Now, I'm going to ask you for three lines to save to file. Make them good!"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "File closed. If only I could be so grossly incandescent."
target.close()
print "Do you want to check the results?"
print "If you do, hit RETURN. If you don't, and want to leave, hit CTRL-C (^C)."

raw_input("?")
print "Opening file..."
target = open(filename)
print target.read()
target.close()

print "Press ENTER to leave."
raw_input("\[T]/")
quit()